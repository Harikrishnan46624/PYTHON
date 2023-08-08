dict1={"NFLX":4950,
       "TREX":2400,
       "FIZZ":1800,
        "XPO":1700}


new_dict = {k: v for k, v in dict1.items() if v > 2000}

print(new_dict)