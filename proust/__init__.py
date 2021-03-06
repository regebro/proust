def main():
    import sys
    import imp
    import argparse
    from timeit import default_timer, Timer
    
    from proust.benchmark import Benchmark
    from proust.suite import Suite
    
    try:
        implementation = sys.implementation.name
    except AttributeError:
        try:
            implementation = sys.subversion[0]
        except AttributeError:
            import os
            import string
            implementation = sys.executable.split(os.path.sep)[-1]
            implementation = ''.join([x for x in implementation if x not in string.digits])
            if implementation == 'python':
                implementation = 'CPython'
        
    platform = '%s %s' % (implementation, '.'.join([str(x) for x in sys.version_info[:3]]))
    
    parser = argparse.ArgumentParser(description="A benchmark runner")
    
    parser.add_argument('filename', help="The file containing the benchmark or suite")
    parser.add_argument('benchmark', help="The name of the benchmark or suite to run")
    parser.add_argument('-o', '--output', help="Output file, default is stdout")
    # Parameter list?
    
    args = parser.parse_args()
    
    module = imp.load_source('bench_module', args.filename)
    benchmark = getattr(module, args.benchmark, None)
    if benchmark is None:
        raise ValueError('Could not find benchmark %s in file %s' % (args.benchmark, args.filename))
    
    if not isinstance(benchmark, (Benchmark, Suite)):
        raise ValueError('%s is not a benchmark or suite.' % (args.benchmark))
    
    results = benchmark.run()
    if not isinstance(results, list):
        # This is from a benchmark. We just wrap it in a list, so we can
        # treat it the same as if it was from a suite.
        results = [results]
    
    # The results are printed out as CVS, but the CVS module is not used,
    # because it's a lot of work to get working on both Python 2 and Python
    # 3, and we don't really need it as the format is simple and predictable.
    if args.output is None:
        output = sys.stdout
    else:
        output = open(args.output, 'wt')
        
    try:
        output.write(results[0].csv_header() + '\n')
        for r in results:
            output.write(r.csv_data() + '\n')
    except Exception:
        if args.output:
            output.close()
        raise

if __name__ == '__main__':
    main()
    