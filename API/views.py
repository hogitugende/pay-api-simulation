from django.shortcuts import HttpResponse
from json import dumps as jsonify
from .models import InfoTransaction

def check(request, id_transaction):
    transaction = InfoTransaction.objects.get(serie=id_transaction)
    donnees = []
    if transaction:
        data = {
			"nom" : transaction.nom,
			"prenom" : transaction.prenom,
			"date" : str(transaction.date),
			"source" : transaction.source,
			"destination" : transaction.destination,
			"montant" : transaction.montant,
			"objet" : transaction.objet,
			"serie" : transaction.serie,
        }
        donnees.append(data)
        json = jsonify(donnees)
        return HttpResponse(json , content_type="application/json")
    return HttpResponse(None, content_type="application/json")


