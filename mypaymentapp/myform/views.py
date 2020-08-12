""" This is the views file """
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import  CardFormNew #pylint:disable=relative-beyond-top-level
from .models import Card #pylint:disable=relative-beyond-top-level

def index(request): #pylint:disable=unused-argument
    """ This is the return method for the status 200,
    which means that the form got saved within the DB"""
    return HttpResponse("200 OK")

def process_payment(request):
    """As we dont' have the APIs, I prefered to leave things nested into many blocks."""
    try: #pylint:disable=unreachable,too-many-nested-blocks
        if request.method == 'POST':
            form = CardFormNew(request.POST)
            if form.is_valid():
                creditcard_number = form.cleaned_data['creditcard_number'] #pylint:disable=unused-variable
                card_holder = form.cleaned_data['card_holder'] #pylint:disable=unused-variable
                expiration_date = form.cleaned_data['expiration_date'] #pylint:disable=unused-variable
                security_code = form.cleaned_data['security_code'] #pylint:disable=unused-variable
                amount = form.cleaned_data['amount'] #pylint:disable=unused-variable

                form.save()
                return HttpResponseRedirect('thanks')
                return HttpResponse(status=200)   #pylint:disable=unreachable     
                #Payment to be processed by different providers
                #Gateway checks and API stuff
                #this is dummy code as we dont have an actual API for mocking
                resp = requests.post(my_endpoint_var, headers=header_var, data=form) #pylint:disable=unreachable,undefined-variable
                if amount < 20:    #pylint:disable=trailing-whitespace
                    try: #pylint:disable=unreachable 
                        print("go to Cheap Payment Gateway")
                        if resp.ok: #pylint:disable=unreachable 
                            print('OK!')
                        else: #pylint:disable=unreachable 
                            print('Oh Noo!')
                    except: #pylint:disable=unreachable,bare-except
                        print('Damn it!')
                elif amount > 20 and amount < 500: #pylint:disable=unreachable,chained-comparison
                    try:
                        print("go to Expensive Payment Gateway")
                    except: #pylint:disable=unreachable,bare-except
                        print("retry only once with Cheap Payment Gateway")
                else: #pylint:disable=unreachable 
                    try: #pylint:disable=unreachable 
                        print("go to Expensive Payment Gateway")

                    except:    #pylint:disable=trailing-whitespace,bare-except            
                        i = 0 #pylint:disable=unreachable 
                        for i in range(3): #pylint:disable=unreachable 
                            print("retry 3 times ")
                            if resp.status_code == 200: #pylint:disable=unreachable 
                                print('OK!')
                                break #pylint:disable=unreachable 
                            i += 1       

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CardFormNew()
            return render(request, 'name.html', {'form':form})
        return render(request, 'name.html', {'form': form})

    #400 error
    except Card.DoesNotExist:
        return HttpResponse(status=404) #pylint:disable=trailing-whitespace
    #500 error
    except:  #pylint:disable=trailing-whitespace,bare-except 
        return HttpResponse(status=500)
    finally:
        print("Hope you enjoyed working with us!")
