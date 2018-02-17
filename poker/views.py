from django.http import HttpResponse, Http404
from django.shortcuts import render

from .libs import THAssistant

## For use by chipDist views without having to send though a template
## Just a constant
chipArrayLen = 6

def index(request):
    title = "Poker Index"

    return render(request, 'poker/index.html', {
        'title': title,
    })

def blindsStructure(request):
    title = "Blinds Structure Calculator"

    return render(request, 'poker/blinds.html', {
        'title': title,
    })

def stackCalculator(request):
    title = "Initial Stack Calculator"

    return render(request, 'poker/stackCalc.html', {
        'title': title,
        'valArray': [0 for i in range(chipArrayLen)],
    })

def chipDistribution(request):
    title = "Chip Distribution Calculator"

    return render(request, 'poker/chipDist.html', {
        'title': title,
        'valArray': [0 for i in range(chipArrayLen)],
    })

def prizePoolDistribution(request):
    title = "Prize Pool Distribution Calculator"

    return render(request, 'poker/prizeDist.html', {
        'title': title,
    })

def processBlinds(request):

    try:
        startingStack = int(request.POST['stack'])
        hours = int(request.POST['hours'])
        if startingStack == 0: raise ValueError("The stack must be greater than 0")
    
    except ValueError as e:
        return HttpResponse(e.args)

    else:
        director = THAssistant.THAssistant()
        structure, period = director.blindsStructure(startingStack, hours)
        title = "Blinds Structure"

        return render(request, 'poker/blindsStructure.html', {
            'title': title,
            'hours': hours,
            'stack': startingStack,
            'structure': structure,
            'period': period,
        })

def processChipDist(request):

    try:
        startingStack = int(request.POST['stack'])
        if startingStack == 0: raise ValueError("The stack must be greater than 0")

        # Get chip values
        chipArray = []
        for i in range(chipArrayLen):
            chipArray.append(int(request.POST['chip_' + str(i)]))

    except ValueError as e:
        return HttpResponse(e.args)

    else:
        director = THAssistant.THAssistant()
        title = "Chip Distribution"

        return render(request, 'poker/chipDistribution.html', {
            'title': title,
            'stack': startingStack,
            'chipDistribution': director.chipDist(startingStack, chipArray),
        })

def processStackCalc(request):

    try:
        bb = int(request.POST['bb'])

        ## Get chip values
        chipArray = []
        for i in range(chipArrayLen):
            chipArray.append(int(request.POST['chip_' + str(i)]))

        if bb <= 1: raise ValueError("The big blind must be greater than 1")

    except ValueError as e:
        return HttpResponse(e.args)

    else:
        director = THAssistant.THAssistant()
        stackSize = director.stackCount(bb, chipArray)
        title = "Initial Stack"

        return render(request, 'poker/initialStack.html', {
            'title': title,
            'bb': bb,
            'stack': stackSize,
            'chipVals': chipArray,
            })

def processPrize(request):

    try:
        dist = str(request.POST['dist'])
        prizepool = int(request.POST['pp'])
        payable = int(request.POST['payable'])
        players = int(request.POST['players'])

        if prizepool == 0: raise ValueError("The prizepool must be greater than 0")

    except ValueError as e:
        return HttpResponse(e.args)

    else:
        director = THAssistant.THAssistant(players, prizepool, payable)
        title = "Prize Pool Distribution"

        return render(request, 'poker/prizeDistribution.html', {
            'title': title,
            'distType': dist,
            'dist': director.prizeDist(dist),
        })
