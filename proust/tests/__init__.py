def get_suite():
    import unittest
    from proust.tests import test_benchmark
    from proust.tests import test_suite
    from proust.tests import test_runner
    from proust.tests import test_main
    
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_benchmark)
    suite.addTests(loader.loadTestsFromModule(test_suite))
    suite.addTests(loader.loadTestsFromModule(test_runner))
    suite.addTests(loader.loadTestsFromModule(test_main))
    return suite