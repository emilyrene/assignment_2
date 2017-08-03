from datetime import datetime, date
from functools import reduce as reduce


def func_list_to_dict(list):    #Step 3: function to convert list to dictionary with date and taxon
    return {'date': datetime.strptime( list[1], "%Y:%m:%d:%H:%M:%S" ), 'taxon': list[22]}

# def reduce_counts(dict_of_counts, filter_dict):        #STEP4: reduce function COUNTS for taxon attempt
#     dict_of_counts = {}
#     for x in filter_dict:
#         dict_of_counts[x] = dict_of_counts.get(x, 0) + 1     #wasn't working because you can't (.get) on filter object or list
#         return dict_of_counts
#
# def x(a, b):
#     counts = {}
#     for x in a:
#         if x in b:
#             x[counts] = sum(1 for x in a if x == b)
#             return counts

# sum( 1 for d in my_list if d.get( 'id' ) == 1 )


dict_of_counts = {}
li_of_dicts = []
with open( 'cleaned_GPMDB_table.tsv', 'r' ) as f:
    header = f.readline()                       #header = so header/ top line is stored
    for line in f:
        li_of_dicts.append( line.strip().split( '\t' ) )
    mapped_dicts = map( func_list_to_dict, li_of_dicts )    #map to only have date and taxon
    start_date = datetime( 2010, 6, 1 )
    end_date = datetime( 2010, 9, 30 )
    filter_dicts = filter(lambda x: start_date <= x['date'] <= end_date, mapped_dicts) #filtering so only date/ taxons are for stated dates are aggregated
    print(list(filter_dicts)) #print to show I got up to here
    # reduce_dict = reduce(x(next(filter_dicts['taxon']), dict_of_counts),filter_dicts,{}) #STEP 4 attempt put next because filter wasnt working

