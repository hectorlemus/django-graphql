import graphene
from players.models import *
from .types import *

class CreateTeamMutation(graphene.Mutation):
  
    class Input:
        name = graphene.String()
        
    name = graphene.Field(TeamType)
    
    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        obj = Team.objects.create(name=name)
        return CreateTeamMutation(name=obj)
        

class CreatePlayerMutation(graphene.Mutation):
    
    class Input(object):
        name = graphene.String()
        age = graphene.Int()
        rating = graphene.Int()
        team_id = graphene.Int()
    
    name = graphene.Field(PlayerType)
    
    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        age = kwargs.get('age', 0)
        rating = kwargs.get('rating', 0)
        team_id = kwargs.get('team_id', 0)
        
        obj = Player.objects.create(name=name, age=age,
            rating=rating, team_id=team_id)
            
        return CreatePlayerMutation(name=obj)
        
class Mutation(graphene.AbstractType):
    create_team = CreateTeamMutation.Field()
    create_player = CreatePlayerMutation.Field()