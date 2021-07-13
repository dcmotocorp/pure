
# import requests
# import time 
# add tyeh sejfdljglojdjo
# def measure_time_100():
#     start= time.time()
#     for number in range(100):
#         requests.get('http://127.0.0.1:8000/worker2/user/2')
#     end=time.time()
#     total_time= end - start  
#     return f'toal time ={total_time}'

# def measure_time_10():
#     start= time.time()
#     for number in range(10):
#         requests.get('http://127.0.0.1:8000/worker2/user/2')
#     end=time.time()
#     total_time= end - start  
#     print(total_time)
#     return  total_time 



# def measure_time_500():
#     start= time.time()
#     for number in range(500):
#         requests.get('http://127.0.0.1:8000/worker2/user/2')
#     end=time.time()
#     total_time= end - start  
#     return f'toal tim{total_time}'


# def measure_time_1000():
#     start= time.time()
#     for number in range(1000):
#         requests.get('http://127.0.0.1:8000/worker2/user/2')
#     end=time.time()
#     total_time= end - start  
    
#     return f'toal time ={total_time}'


# if __name__ == '__main__':
#     measure_time_10()

import requests


def test_100():
    for _ in range(100):
        resp = requests.get('http://127.0.0.1:8000/worker2/lists/')



if __name__ == '__main__':
    import time

    start_time = time.time()

    test_100()
    print(f"--- {time.time() - start_time} seconds for 100 sequential urls ---")

