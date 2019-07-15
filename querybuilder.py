'''
This class is designed to go along with a class to collect input and construct the calls to the functions q_id etc,
 a class to connect to the database and execute the query and a class to display the gathered data
'''

class QueryBuilder:

    def __init__(self, tablename):
        self.tablename = tablename
        self.conditions = []
        self.query = ''

    def q_id(self, *args, condition='=', prefix='AND'):
        comparisons = {'=', '<', '>'}
        if len(args) == 1 and not type(args[0]) is list and condition in comparisons:
            self.conditions.append(['id' + condition + str(args[0]), prefix.upper()])

        elif len(args) == 2 and (type(args[0]) is int and type(args[1]) is int):
            self.conditions.append(["(id BETWEEN " + str(args[0]) + " AND " + str(args[1]) + ')', prefix.upper()])

        elif len(args) == 1 and condition.lower() == 'in' and type(args[0]) is list:
            mylist = '(' + ', '.join(str(e) for e in args[0]) + ')'
            self.conditions.append(["id IN " + mylist, prefix.upper()])
        elif len(args) == 1 and condition.lower() == 'notin' and type(args[0]) is list:
            mylist = '(' + ', '.join(str(e) for e in args[0]) + ')'
            self.conditions.append(["id NOTIN " + mylist, prefix.upper()])
        else:
            print('invalid arguments')

    def q_url(self, url, prefix='AND'):
        self.conditions.append(["url=" + url, prefix.upper()])

    def q_date(self, *args, condition='=', prefix='AND'):

        if len(args) == 1:
            self.conditions.append(['date' + condition + str(args[0]), prefix.upper()])
        elif len(args) == 2:
            self.conditions.append(["(date BETWEEN " + str(args[0]) + " AND " + str(args[1]) + ')', prefix.upper()])
        else:
            print('invalid arguments')

    def q_rating(self, *args, condition='=', prefix='AND'):

        if len(args) == 1:
            self.conditions.append(['rating' + condition + str(args[0]), prefix.upper()])
        elif len(args) == 2:
            self.conditions.append(["(rating BETWEEN " + str(args[0]) + " AND " + str(args[1]) + ')', prefix.upper()])
        else:
            print('invalid arguments')

    def build_select_query(self):
        if len(self.conditions) == 0:
            print('First add conditions.')
            return
        elif self.query != '':
            print('Please flush query before building another.')
            return

        self.query = 'SELECT * FROM ' + self.tablename + ' WHERE ' + self.conditions[0][0]

        for i in range(1, len(self.conditions)):
            self.query = self.query + ' ' + self.conditions[i][1] + ' ' + self.conditions[i][0]

        return self.query

    def flush(self):
        self.conditions = []
        self.query = ''


if __name__ == '__main__':

    builder = QueryBuilder('tablename')

    builder.q_id(10, condition='>', prefix='Or')
    builder.q_url('www.url.com')
    builder.q_id([1,2,3,4], condition='IN', prefix='or')
    print(builder.build_select_query())
    builder.flush()
    builder.q_date(10, 5, prefix='AND')
    print(builder.build_select_query())
