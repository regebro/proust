
class Runner(object):
    """The runner runs a benchmark or a suite and saves the results."""
     
    #def run(self, suite, platforms, **kw):
        #for platform in platforms:
            #platform.run(suite, **kw)

    #def save(self, outfile):
        #fields = sorted(self.results[0]['kw'].keys())
        #outfile.write('Description,Platform,')
        #for field in fields:
            #outfile.write('%s,' % field.title())
        #outfile.write('Count,Max,Min,Average,Median\n')
        
        #for result in sorted(self.results, key=lambda x: x['kw']):
            #outfile.write('"%s",%s,' % (self.description, platform))
            #for field in fields:
                #outfile.write('%s,' % result['kw'][field])
            #outfile.write('%s,%s,%s,%s,%s' % (result['count'],result['max'],result['min'],result['average'],result['median']))
                
    #def warmup(self):
        ## Run a loop for a second to make any processor wake up.
        #cumul_time = 0
        #while True:
            ## Warmup: 
            #start = timer()
            #y = 0
            #for x in range(1000):
                #y += x
            #time = timer() - start
            #cumul_time += time
            #if cumul_time > 1:
                #break
             
    #def __str__(self):
        #res = []
        #for result in sorted(self.results, key=lambda x: x['kw']):
            #res.append('%s Params: %s Count: %s Min: %s Max %s' % (self.description, result['kw'], result['count'], result['min'], result['max']))
            
        #return '\n'.join(res)
