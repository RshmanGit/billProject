import time
from api.models import *
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

#fetch all fetched=false entries and update them true
def fetch_and_update_order(ref):
    try:
        result = ref.order_by_child('Fetched').equal_to("false").get()
        for i in result:
            try:
                #print("[+] Adding new value")
                #print(type(result[i]['Order Date']))
                #print(type(result[i]['Delivery Date']))
                neworder = order()
                neworder.customer_name = result[i]['Customer Name']
                neworder.product_name = result[i]['Product Name']
                neworder.village = result[i]['Village']
                neworder.quantity = result[i]['Quantity']
                neworder.order_date = datetime.strptime(result[i]['Order Date'],"%d/%m/%Y")
                neworder.delivery_date = datetime.strptime(result[i]['Delivery Date'],"%d/%m/%Y")
                neworder.mobile_number = int(result[i]['Mob No'][1:])
                neworder.save()
                post = ref.child(i)
                post.update({

                    'Fetched' : 'true'

                })
                print("[+]Value added and updated")
            except Exception as e:
                print(str(e))
                print("[-]value adding error")
    except Exception as e:
        print("[-]Error occured")
        print(e)

#fetch and update all expenses
def fetch_and_update_expenses(ref):
    try:
        result = ref.order_by_child("Fetched").equal_to("false").get()
        for i in result:
            try:
                print("[+] Adding new expenses")
                newexpenses = expenses()
                newexpenses.desc = result[i]['Description']
                newexpenses.cost = result[i]['Cost:']
                newexpenses.cashInHand = result[i]['Cash in Hand']
                newexpenses.date = datetime.strptime(result[i]['Date'],"%d/%m/%Y")
                newexpenses.save()
                post = ref.child(i)
                post.update({

                    'Fetched' : 'true'

                })
                print("[+]Value added and updated")
            except Exception as e:
                print("Error in adding expense")
    except Exception as e:
        print(e)
        print("[-]Error occured")

#fetch and update all raw material orders
def fetch_and_update_rawmat(ref):
    try:
        result = ref.order_by_child('Fetched').equal_to("false").get()
        for i in result:
            try:
                print("[+] Adding new rawmat")
                newrawmat = rawMaterialOrder()
                newrawmat.gatePass = result[i]['GatePass']
                newrawmat.name = result[i]['Raw Material']
                newrawmat.desc = result[i]['Description']
                newrawmat.weight = result[i]['Weight']
                newrawmat.order_date = datetime.strptime(result[i]['Order Date:'],"%d/%m/%Y")
                newrawmat.save()
                post = ref.child(i)
                post.update({

                    'Fetched' : 'true'

                })
                print("[+]Value added and updated")
            except Exception as e:
                print(str(e))
                print("[-]raw material cant be added")
    except Exception as e:
        print(e)
        print("[-]Error occured")

#post all pending orders in firebase
def post_all_pending_orders(ref):
    try:
        pending_orders = order.objects.filter(delivered = False)
        fmt = '%d/%m/%Y'

        #clearing old data before posting
        try:
            ref.set({})
            #time.sleep(3)
        except Exception as e:
            print(e)
            print('[-]Error occured')

        for o in pending_orders:
            try:
                print("[+]Order pushing")
                ref.push({
                    "id" : o.id,
                    "customer_name" : o.customer_name,
                    "product_name" : o.product_name,
                    "village" : o.village,
                    "quantity" : o.quantity,
                    "order_date" : o.order_date.strftime(fmt),
                    "delivery_date" : o.delivery_date.strftime(fmt),
                    "quant_delivered" : o.quant_delivered,
                    "mobile_number" : o.mobile_number,
                    "delivered" : o.delivered
                })
            except Exception as e:
                print(e)
                print("[-]Error occured")
    except Exception as e:
        print(e)
        print("[-]Error occured")

def do():
    print("[+]cron begins\n")
    #firebase configurations
    cred = credentials.Certificate("abhaychem-7159f-firebase-adminsdk-am6xd-384b8b166d.json")
    firebase_admin.initialize_app(cred,{
        'databaseURL' : 'https://abhaychem-7159f.firebaseio.com/'
    })
    order_ref = db.reference('Order Details')

    rawmat_ref = db.reference('Raw Details')
    exp_ref = db.reference('Expenses Details')

    pend_ref = db.reference('Pending orders')

    while(True):
        time.sleep(300)
        print("[+]Cron started")
        try:
            print("[+]fetching orders")
            fetch_and_update_order(order_ref)
            print("[+]orders updated")
            print("[+]fetching raw material")
            fetch_and_update_rawmat(rawmat_ref)
            print("[+]raw materials updated")
            print("[+]fetching expenses")
            fetch_and_update_expenses(exp_ref)
            print("[+]expenses updated")
        except Exception as e:
            print("[-]Error")
            print(e)

        try:
            print("[+]Posting all pending orders")
            post_all_pending_orders(pend_ref)
            print("[+]Posted all pending orders")
        except Exception as e:
            print(e)
            print("[-]Error occured while posting pending orders")

        print("[+]Cron terminated")
