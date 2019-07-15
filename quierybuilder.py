'''
We have a sql table with 4 columns (id, url, date, rating). We need a set of classes that allows
us to build a query which can filter this table across any combination of these possibilities:
● id: >, <, =, IN, NOTIN
● url: =
● date: >, <, =
● rating: >, <, =
E.g. we may want all entries with: (2 < rating < 9) and (id in list) and (date > 1 Jan 2016).
The goal is to have a set of classes which enable easy testing wherever they are used (i.e. the
database does not have to be overly mocked every time). We want users of these classes to be
able to add filters without having to add to or rewrite tests.
'''


class QueryBuilder:

    def __init__(self, tablename):
        self.tablename = tablename
        self.conditions = []
        self.query = ''

    def q_id(self, *args, condition='=', prefix='AND'):

        if len(args) == 1 and not type(args[0]) is list:
            self.conditions.append(['id' + condition + str(args[0]), prefix.upper()])

        elif len(args) == 2 and not (type(args[0]) is list or type(args[1]) is list):
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

    def buildSelectQuery(self):
        if len(self.conditions) == 0:
            print('First add conditions.')
            return ''
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

    builder.q_id(10, 11, condition='<')
    builder.q_url('www.url.com')
    builder.q_id([1,2,3,4], 2, 2, condition='IN', prefix='or')
    builder.buildSelectQuery()
    print(builder.buildSelectQuery())
