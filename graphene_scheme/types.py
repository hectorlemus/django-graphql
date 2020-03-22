import graphene 
from graphene_django.types import DjangoObjectType
from players.models import Team, Player

class TeamType(DjangoObjectType):
  class Meta:
    model = Team

class PlayerType(DjangoObjectType):

  class Meta:
    model = Player
    
class Query(object):
    player = graphene.Field(PlayerType,
        id=graphene.Int(),name=graphene.String())

    all_teams = graphene.List(TeamType)
    all_players = graphene.List(PlayerType)
    
    def resolve_all_teams(self, info, **kwargs):
        return Team.objects.all()  
    
    def resolve_all_players(self, info, **kwargs):
        return Player.objects.select_related('team').all()  
    
    def resolve_player(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')
        if id is not None:
            return Player.objects.select_related('team').get(pk=id)
        
        if name is not None:
            return Player.objects.select_related('team').get(name=name)
        
        return None