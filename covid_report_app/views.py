from django.shortcuts import render
from requests_html import HTML, HTMLSession

def home(request):
	session = HTMLSession()
	# r = session.get('')
	url = session.get('https://www.mohfw.gov.in/')

	obj = url.html.find('#main-content')
	# ul = obj.ul.li
	# site_dashboard = obj.find('strong')
	for obj in obj:
		grabing_site_dashboard = obj.find('#site-dashboard', first = True)
		grabing_container = grabing_site_dashboard.find('.container', first = True)
		status_update = grabing_container.find('.status-update', first=True) #for status update time 
		grab_h2_span_in_status_update = status_update.find('h2 span', first= True) #for status update time

		grabing_ul = grabing_container.find('ul', first = True)
		#its hard to differenciate list after looping 
		# so its impportant to fetch them one by one
		active_cases = grabing_ul.find('li strong')[0]
		cured_cases = grabing_ul.find('li strong')[1]
		death_cases = grabing_ul.find('li strong')[2]
		migrate_cases = grabing_ul.find('li strong')[3]
		
		# status_update = grabing_container.find('.status-update')
		# finding_h2 = status_update.find('h2')
		# finding_span = status_update.find('span')
		# print(finding_span)



	context = {
				'grab_h2_in_status_update':grab_h2_span_in_status_update,
				'active_cases':active_cases,
				'cured_cases':cured_cases,
				'death_cases':death_cases,
				'migrate_cases':migrate_cases,
				}
	template_name = 'covid_report_app/home.html'
	return render(request, template_name, context)	