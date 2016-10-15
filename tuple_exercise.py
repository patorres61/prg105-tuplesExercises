# Phyllis Torres
# Tuple Exercises
# Due Date: October 20, 2016

# define colors and bold text parameters
class color:
    def __init__(self):
        pass
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# This program takes records from the assignment to create lists and tuples

# print title of program and name
print color.BOLD + '\nTuple Exercises\n' + color.END
print('Phyllis Torres\n')

print('This program creates lists and tuples from records given in the assignment. ')
print('Then, specific fields are selected to print from each record.')

# create a tuple for each record given in the assignment

# the following code creates tuples for the parts records
parts_hdr = ('Part ID', 'Part', 'Room', 'Cabinet Location', 'Vendor ID', 'Price', 'Quantity in Stock')
parts_t1 = ('T-01', 'Tower Case', 'S110', 'Cabinet B, Shelf 1', 'V-010', 79.99, 3)
parts_t2 = ('P-02', 'CPU', 'S110', 'Drawer', 'V-010', 199.99, 2)

# the following code creates tuples for the text book records
text_hdr = ('Textbook ID', 'Textbook Name', 'Courses', 'Number of Books', 'Price Per Book', 'Publisher ID')
text_t1 = ('TEXT-0001', 'Basic Anatomy and Physiology', 'BIO-100', 400, 94, 'PUB-1003')
text_t2 = ('TEXT-0002', 'Chemistry for Biology Students', 'BIO-101-102', 400, 105.30, 'PUB-1002')
text_t3 = ('TEXT-0003', 'Anatomy and Physiology', 'BIO-141-142', 330, 159.75, 'PUB-1003')

# create tuples for the publisher records
pub_hdr = ('Publisher ID', 'Publisher Name', 'Address', 'City', 'State', 'Zip Code', 'Phone Number')
pub_t1 = ('PUB-1001', 'Science Books Galore', '525 Allen St.', 'Trenton', 'NJ', 8620, '(609) 555-2554')
pub_t2 = ('PUB-1002', 'Books for Chemistry Students Ltd.', '142 N. Spring St.', 'Los Angeles', 'CA', 90012, '(213) 555-8362')
pub_t3 = ('PUB-1003', 'Carliz Publishers Corp.', '24 King Ave.', 'Columbus', 'OH', 43201, '(614) 555-3322')

# create the tables from the tuple records
parts_tbl = [parts_hdr, parts_t1, parts_t2]

text_tbl = [text_hdr, text_t1, text_t2, text_t3]

pub_tbl = [pub_hdr, pub_t1, pub_t2, pub_t3]

print('\nPrint the following fields - Part Id, Price, and Quantity in Stock, from the Parts Database: \n')

# the following code loops through the parts table and creates a list of the desired fields
# the index for the first record of the table must begin with zero
# the index for the first element of the record must also begin with zero
index = 0

# create an empty list
parts = []

# loop through the parts database and pull the part id, price, and quantity in stock
while index < len(parts_tbl):
    parts.append(parts_tbl[index][0])
    parts.append(parts_tbl[index][5])
    parts.append(parts_tbl[index][6])
    index += 1
    print parts
    # initialize the print list to an empty list
    parts = []


print('\nPrint the following fields - Textbook Name and Price, from the Textbook Database: \n')

# the following code loops through the textbook table and creates a list of the desired fields
# the index for the first record of the table must begin with zero
# the index for the first element of the record must also begin with zero
indx2 = 0

# create an empty list
texts = []

# loop through the textbook database and pull the textbook name and price
while indx2 < len(text_tbl):
    texts.append(text_tbl[indx2][1])
    texts.append(text_tbl[indx2][4])
    indx2 += 1
    print texts
    # initialize the print list to an empty list
    texts = []

print('\nPrint the following fields - Publisher Name and Phone Number, from the Publisher Database: \n')

# the following code loops through the publisher database and creates a list of the desired fields
# the index for the first record of the table must begin with zero
# the index for the first element of the record must also begin with zero
indx3 = 0

# create an empty list
pub = []

# loop through the publisher database and pull the publisher name and phone number
while indx3 < len(pub_tbl):
    pub.append(pub_tbl[indx3][1])
    pub.append(pub_tbl[indx3][6])
    indx3 += 1
    print pub
    # initialize the print list to an empty list
    pub = []





