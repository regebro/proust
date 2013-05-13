class Result(object):
    def __init__(self, count, fastest, cumul_time, iterations, keywords, description):
        self.count = count
        self.fastest = fastest
        self.cumul_time = cumul_time
        self.iterations = iterations
        self.keywords = keywords
        self.description = description
        
    def csv_data(self):
        description = self.description.replace('"', '\"')
        res = '"%s",%s,%s,%s,%s' % (description, self.count, self.fastest, self.cumul_time, self.iterations)
        keywords = ','.join([str(self.keywords[x]) for x in sorted(self.keywords)])
        if keywords:
            res += ',' + keywords
        return res
    
    def csv_header(self):
        res = 'Description,Count,Fastest,Total time,Iterations'
        keywords = ','.join([str(x) for x in sorted(self.keywords)])
        if keywords:
            res += ',' + keywords
        return res
    
    def __eq__(self, other):
        if not isinstance(other, Result):
            return NotImplemented
        return self.__dict__ == other.__dict__
