import csv

fh = open('whc-sites-2018-small.csv')
rows = csv.reader(fh)

Category.objects.all().delete()
State.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()
Site.objects.all().delete()


for row in reader:

    print(row)

    try:
        c = Category.objects.get(name=row[7])
    except:
        print("Inserting category", row[7])
        c = Category(name=row[7])
        c.save()

    try:
        st = State.objects.get(name=row[8])
    except:
        print("Inserting State",row[8])
        st = State(name=row[8])
        st.save()

    try:
        r = Region.objects.get(name=row[9])
    except:
        print("Inserting Region",row[9])
        r = Region(name=row[9])
        r.save()

    try:
        i = Iso.objects.get(name=row[10])
    except:
        print("Inserting ISO",row[10])
        i = Iso(name=row[10])
        i.save()

    try:
        y = int(row[3])
    except:
        y = None

    try:
        lo = float(row[4])
    except:
        lo = None

    try:
        la = float(row[5])
    except:
        la = None

    try:
        ah = float(row[6])
    except:
        ah = None

    site = Site(name=row[0],description=row[1], justification=row[2], year=y, longitude=lo, latitude=la, area_hectares=ah, category=c, states=st, region=r, iso=i)
    site.save()

