from django_cassiopeia import cassiopeia as cass
from django.http import JsonResponse
from django.views import View

class SummonerView(View): # Django CBV with json response
    def get(self, request):
        summoner = cass.Summoner(name="Kalturi")
        return JsonResponse({"name": summoner.name, "level": summoner.level})