from django.core.management.base import BaseCommand, CommandError
from clients.models import Client
from companys.models import Company
from rents.models import Rent

class Command(BaseCommand):
    help = 'populate db'

    # def add_arguments(self, parser):
    #     parser.add_arguments()

    def handle(self, *args, **options):
        

        
        c1=Client(rut='18620855-1', name='Angel Serrano' )
        c1.save()
        c2=Client(rut='11345435-2', name='Roser Abreu' )
        c2.save()
        c3=Client(rut='14256777-k', name='Rosa Campos' )
        c3.save()
        c4=Client(rut='12675688-0', name='Celestino Fuentes' )
        c4.save()
        c5=Client(rut='14234334-4', name='Rebeca Rojas' )
        c5.save()
        c6=Client(rut='10152323-8', name='Andrea Palomo' )
        c6.save()
        c7=Client(rut='15587715-4', name='Maria Inmaculada Jiménez' )
        c7.save()
        c8=Client(rut='15034590-7', name='Marcela Navarro' )
        c8.save()
        c9=Client(rut='11804345-3', name='Francisco Manuel Gago' )
        c9.save()
        c10=Client(rut='13804238-0', name='Patricio Duran' )
        c10.save() 
        
        # company = Company.objects.bulk_create([
        #     Company(name= 'CHILE ARRIENDA AUTOS S.A' ),
        #     Company(name= 'AUTOK S.A' ),
        #     Company(name= 'RENT A CAR S.A' ),
        # ])

        co1=Company(name="CHILE ARRIENDA AUTOS S.A")
        co1.save()
        co2=Company(name="AUTOK S.A'")
        co2.save()
        co3=Company(name="RENT A CAR S.A")
        co3.save()




        rent = Rent.objects.bulk_create([
           Rent(client= c6, company=co1, daily_cost= 15000, days= 3),
           Rent(client= c1, company=co3, daily_cost= 18000, days= 2),
           Rent(client= c5, company=co3, daily_cost= 135000, days= 1), 
           Rent(client= c2, company=co2, daily_cost= 5600, days= 4),
           Rent(client= c3, company=co1, daily_cost= 23000, days= 3),
           Rent(client= c7, company=co2, daily_cost= 15000, days= 3),
           Rent(client= c8, company=co3, daily_cost= 45900, days= 2),
           Rent(client= c10, company=co3, daily_cost= 19000, days= 5),
           Rent(client= c9, company=co3, daily_cost= 51000, days= 7),
           Rent(client= c5, company=co1, daily_cost= 89000, days= 7),
           Rent(client= c1, company=co2, daily_cost= 16000, days= 1),
           Rent(client= c3, company=co3, daily_cost= 37500, days= 1),
           Rent(client= c6, company=co1, daily_cost= 19200, days= 2),
           Rent(client= c6, company=co3, daily_cost= 10000, days= 3),
           Rent(client= c6, company=co2, daily_cost= 5900, days= 2),
           Rent(client= c10, company=co1, daily_cost= 9000, days= 5),
           Rent(client= c10, company=co3, daily_cost= 13500, days= 5),
           Rent(client= c9, company=co1, daily_cost= 38200, days= 4),
           Rent(client= c7, company=co2, daily_cost= 17000, days= 1),
           Rent(client= c5, company=co3, daily_cost= 1000, days= 10),
           Rent(client= c1, company=co2, daily_cost= 6000, days= 20),
           Rent(client= c3, company=co1, daily_cost= 16200, days= 7),
           Rent(client= c2, company=co2, daily_cost= 10000, days= 5),
        ])

        
        print("populate DB")