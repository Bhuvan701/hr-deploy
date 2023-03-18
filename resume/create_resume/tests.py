context = {
						'post_applied' : request.POST['post_applied'],
						'dob' : request.POST['dob'],
						'dept' : request.POST['dept'],
						'name'  :request.POST['name'],
						'email' :request.POST['email'],
						'phone' :request.POST['phone'],
						'aadhar':request.POST['aadhar'],
						'f_name' :request.POST['f_name'],
						'm_name' : request.POST['m_name'],
						'f_status' : request.POST['f_status'],
						'f_occupation':request.POST['f_occupation'],
						'm_occupation':request.POST['m_occupation'],
						'b_occupation':request.POST['b_occupation'],
						'address':request.POST['address'],
						'religion':request.POST['religion'],
						'community':request.POST['community'],
						'caste' :request.POST['caste'],
						'marital_status':request.POST['marital_status'],
						's_name' : request.POST['s_name'],
						's_qualification' : request.POST['s_qual'],
						'no_of_child' : request.POST['no_of_child'],
						's_occupation':request.POST['s_occupation'],
						'tenth_spec':request.POST['tenth_spec'],
						'tenth_inst':request.POST['tenth_inst'],
						'tenth_place':request.POST['tenth_place'],
						'tenth_yop':request.POST['tenth_yop'],
						'tenth_per':request.POST['tenth_per'],
						'twelvth_spec':request.POST['twelvth_spec'],
						'twelvth_inst':request.POST['twelvth_inst'],
						'twelvth_place':request.POST['twelvth_place'],
						'twelvth_yop':request.POST['twelvth_yop'],
						'twelvth_per':request.POST['twelvth_per'],
						'diplamo_spec':request.POST['diplamo_spec'],
						'diplamo_inst':request.POST['diplamo_inst'],
						'diplamo_place':request.POST['diplamo_place'],
						'diplamo_yop':request.POST['diplamo_yop'],
						'diplamo_per':request.POST['diplamo_per'],
						'ug_spec':request.POST['ug_spec'],
						'ug_inst':request.POST['ug_inst'],
						'ug_place':request.POST['ug_place'],
						'ug_yop':request.POST['ug_yop'],
						'ug_per':request.POST['ug_per'],
						'pg_spec':request.POST['pg_spec'],
						'pg_inst':request.POST['pg_inst'],
						'pg_place':request.POST['pg_place'],
						'pg_yop':request.POST['pg_yop'],
						'pg_per':request.POST['pg_per'],
						'mphil_spec':request.POST['mphil_spec'],
						'mphil_inst':request.POST['mphil_inst'],
						'mphil_place':request.POST['mphil_place'],
						'mphil_yop':request.POST['mphil_yop'],
						'mphil_per':request.POST['mphil_per'],
						'phd_spec':request.POST['phd_spec'],
						'phd_inst':request.POST['phd_inst'],
						'phd_place':request.POST['phd_place'],
						'phd_yop':request.POST['phd_yop'],
						'phd_per':request.POST['phd_per'],
						'addon_qual':request.POST['addon_qual'],
						'ug_exp':request.POST['ug_exp'],
						'pg_exp':request.POST['pg_exp'],
						'phd_exp':request.POST['phd_exp'],
						'total_exp':request.POST['total_exp'],
						'salary':request.POST['salary'],
						'pic' : img,
					}



<tr>

                        <td>{{p.name}}</td>
                        <td><a href="{% url 'viewresume' p.name %}" target="_blank" class="text-primary">View Application</a></td>
                        <td>{{p.created_at}}</td> 
                        {%if p.viewed %}
                        <td>Viewed</td>
                        {%else%}
                        <td>Not Viewed</td>
                        {%endif%}
                        {%if p.short_listed%}
                        <td>short listed</td>
                        {%else%}
                        <td>Not short listed</td>
                        {%endif%}
                      </tr>