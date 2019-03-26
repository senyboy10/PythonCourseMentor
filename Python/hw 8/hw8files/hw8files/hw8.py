import json
import hw8util

def find_businesses(location, category):
    business_list = []
    business_set = set([])
    for line in open('businesses.json'):
        line = json.loads(line)
        
        i = 0
        for item in line['categories']:
            line['categories'][i] = item.lower()
            i += 1
            
        if ',' in category:
            categorylist = category.split(',')
            [item.strip() for item in categorylist]   
        else:
            if location in line['full_address'] and category == '':
                business_list.append(line)
            elif location in line['full_address'] and category in line['categories']:
                business_list.append(line)
    
           
    categories = set([])
    cat_count = []
    latitude = []
    longitude = []
    for restaurant in business_list:
        for i in range(len(restaurant['categories'])):
            categories.add(restaurant['categories'][i])
            cat_count.append(restaurant['categories'][i])
        latitude.append(restaurant['latitude'])
        longitude.append(restaurant['longitude'])
            
    categories = sorted(categories) 
    num_cat_count = []
    for item in categories:
        num_cat_count.append(cat_count.count(item))
    
    categories = list(categories)
    if len(categories) > 0:
        for i in range(len(num_cat_count)):
            print "\t%s (%d)"%(categories[i].title(), num_cat_count[i])  

    distances = [0]   
    for i in range(len(latitude)-1):
        for j in range(len(longitude)):
            distances.append(hw8util.dist(latitude[i], longitude[i], latitude[j], longitude[j]))

    if category not in categories and not category == '':
        x = "Found 0 businesses, with 0 radius"
        print x
    else:
        x = "Found %d businesses in %.2f radius"%(len(business_list), max(distances))
        print x
        
    return x
        
def print_businesses(location, category):
    business_list = []
    for line in open('businesses.json'):
        line = json.loads(line)
        
        i = 0
        for item in line['categories']:
            line['categories'][i] = item.lower()
            i += 1
            
        if location in line['full_address'] and category == '':
            business_list.append(line)
        elif location in line['full_address'] and category in line['categories']:
            business_list.append(line)
    
    i = 1
    for restaurant in business_list:
        print "%d. %s (%d reviews, %.1f stars) [%s]" %(i, restaurant['name'], restaurant['review_count'], restaurant['stars'], restaurant['full_address'].replace("\n"," "))
        i += 1

if __name__ == '__main__':
    while True:
        print '\n' + '=' *30
        loc = raw_input("Where (-1 to exit) ==> ")
        print loc
        loc = loc.capitalize()
        
        if loc == '-1' or loc == '':
            break
        else:
            category = raw_input("Filter by what ==> ")
            print category
            category = category.lower()
            x = find_businesses(loc, category)
            if x == "Found 0 businesses, with 0 radius":
                continue
            b_print = raw_input("Print the businesses (y/Y)? ==> ")
            print b_print
            if b_print == 'y' or b_print == 'Y':
                print_businesses(loc, category)
            else:
                continue