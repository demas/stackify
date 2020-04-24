alltests: unitest funtest
unitest: ; cd stackify-tests/; PYTHONPATH=.:../stackify pytest unit
funtest: ; cd stackify-tests/; PYTHONPATH=.:../stackify pytest funtest