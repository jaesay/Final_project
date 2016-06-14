from django.shortcuts import get_object_or_404, render
from businesses.models import Business, Goal, Worker, Resource, Finance, Location, Material,Room
from django.shortcuts import render_to_response, HttpResponse
from django.template.context import RequestContext
from chartit import DataPool, Chart
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from models import Goal_score, Finance_score


def goal_chart_view(request, business_id, goal_id):
    goal_data = \
        DataPool(
            series=
            [{'options': {
                'source':  Goal_score.objects.filter(goal_name_id=goal_id)},
                'terms': [
                    'school_year',
                    'goal',
                    'score']}
            ])


    cht = Chart(
        datasource=goal_data,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'school_year': [
                    'goal',
                    'score']
            }}],
        chart_options=
        {'title': {
            'text': 'Data of ' + Goal.objects.get(pk=goal_id).goal_name },
            'xAxis': {
                'title': {
                    'text': 'school_year'}}})

    business = get_object_or_404(Business, pk=business_id)

    context = {'business': business,
               'datachart': cht}

    return render(request, 'businesses/chart.html', context)


def finance_chart_view(request, business_id,finance_id):
    ds = DataPool(
        series=
        [{'options': {
            'source': Finance_score.objects.filter(finance_name_id=finance_id)},
            'terms': [
                'year',
                'goal',
                'price']}
        ])


    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': True,
            'stack': 0},
            'terms': {
                'year': [
                    'goal',
                    {'price': {
                        'stack': 1}},]
            }}],
        chart_options=
        {'title': {
            'text': 'Data of ' + Finance.objects.get(pk=finance_id).name },
            'xAxis': {
                'title': {
                    'text': 'year'}}})

    business = get_object_or_404(Business, pk=business_id)

    context = {'business': business,
               'datachart': cht}

    return render(request, 'businesses/chart1.html', context)



def room(request, business_id, location_id):
    business = get_object_or_404(Business, pk=business_id)
    location = get_object_or_404(Location, pk=location_id)
    context = {'business': business,
               'location': location}
    return render(request, 'businesses/room.html', context)


def reservation(request, business_id, location_id, room_id):
    room = Room.objects.get(pk=room_id)

    if room.reservation == 'Available':
        room.reservation = 'Occupied'
        room.save()

    return HttpResponseRedirect(reverse('businesses:room', args=(business_id,location_id,)))


def room_return(request, business_id, location_id, room_id):
    room = Room.objects.get(pk=room_id)

    if room.reservation == 'Occupied':
        room.reservation = 'Available'
        room.save()

    return HttpResponseRedirect(reverse('businesses:room', args=(business_id,location_id,)))

def material_number(request, business_id,material_id):
    material = Material.objects.get(pk=material_id)

    if material.not_used_number > 0:
        material.not_used_number -= 1;
        material.used_number += 1;
        material.save()
    else:
        material.not_used_number = 0
        material.save()

    return HttpResponseRedirect(reverse('businesses:material', args=(business_id,)))

def material_return(request, business_id,material_id):
    material = Material.objects.get(pk=material_id)

    if material.used_number > 0:
        material.not_used_number += 1;
        material.used_number -= 1;
        material.save()
    else:
        material.used_number = 0
        material.save()

    return HttpResponseRedirect(reverse('businesses:material', args=(business_id,)))



def index(request):
    business_list = Business.objects.all()
    context = RequestContext(request, {'request': request, 'business_list': business_list})
    return render_to_response('businesses/index.html', context_instance=context)

def menu(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/menu.html', {'business': business})


def goal(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/goal_detail.html', {'business': business})

def worker(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/worker_detail.html', {'business': business})

def finance(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/finance_detail.html', {'business': business})

def resource(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/resource_detail.html', {'business': business})

def location(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/location_detail.html', {'business': business})

def material(request, business_id):
    business = get_object_or_404(Business, pk=business_id)
    return render(request, 'businesses/material_detail.html', {'business': business})




