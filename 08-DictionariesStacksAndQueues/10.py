countries = [{
    "country": "Poland",
    "population": "37,38 mil",
   },
{
    "country": "Netherlands",
    "population": "17,53 mil",
},
{
    "country": "Czech Repunlic",
    "population": "10,7 mil",
},
{
    "country": "Czech Repunlic",
    "population": "10,7 mil",
},
{
    "country": "Lithuania",
    "population": "2,795 mil",
},
{
    "country": "Spain",
    "population": "47,33 mil",
}]

i=0
while i<len(countries):
    for k,v in countries[i].items():
        print(v, end=' ')
    print()
    i+=1
