def adjust_to_correct_appdir():
    import os, sys
    try:
        appdir = sys.argv[0] #feel free to use __file__
        if not appdir:
            raise ValueError
        appdir = os.path.abspath(os.path.dirname(sys.argv[0]))
        os.chdir(appdir)
        if not appdir in sys.path:
            sys.path.insert(0,appdir)
    except:
        print('Por favor, execute a partir de um console do sistema operacional.')
        import time
        time.sleep(5)
        sys.exit(1)
adjust_to_correct_appdir()
