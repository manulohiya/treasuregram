from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Treasure
from .forms import TreasureForm

# Create your views here.

def index(request):
	treasures = Treasure.objects.all()
	form = TreasureForm()
	return render(request, 'index.html', {'treasures':treasures, 'form':form})

def detail(request, treasure_id):
	treasure = Treasure.objects.get(id=treasure_id)
	return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
	form = TreasureForm(request.POST, request.FILES)
	if form.is_valid():
		# treasure = Treasure(name = form.cleaned_data['name'],
		# 	value = form.cleaned_data['value'],
		# 	material = form.cleaned_data['material'],
		# 	location = form.cleaned_data['location'],
		# 	img_url = form.cleaned_data['img_url'])
		# treasure.save()
		form.save(commit = True)
	return HttpResponseRedirect('/')

# class Treasure:
# 	def __init__(self, name, value, material, location, img_url):
# 		self.name = name
# 		self.value = value
# 		self.material = material
# 		self.location = location
# 		self.img_url = img_url


# treasure1 = Treasure('Gold Nugget', 500.0, 'gold', "Curly's Creek, NM", 'http://www.clipartkid.com/images/375/gold-nugget-large-gold-nugget-37-9-gm-9DAZWn-clipart.jpg')
# treasure2 = Treasure('Fools Gold Nugget', 0, 'pyrite', 'Fools Falls, CO', 'https://pbs.twimg.com/profile_images/754479423223570432/yWfHOCgc.jpg')
# treasure3 = Treasure('Coffee Can', 20.0, 'tin', 'Acme, CA', 'http://www.antiqueadvertisingexpert.com/wp-content/uploads/2015/03/Old-Judge-Coffee-Tin-Can-.jpg')

# treasures = [treasure1, treasure2, treasure3]
