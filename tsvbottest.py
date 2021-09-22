import twitter as twt

user = twt.Api(consumer_key='FR7pCtcvpmBNHFodiz1ABe1Ve',
               consumer_secret='88zUOUXS1kpD20Y7som9xoCERpfbhezlLc6gaHRmRVk0RaelVM',
               access_token_key='1337349470984437760-ekWY5yFFoWIFLLAZXeYUhHgaSJo6OP',
               access_token_secret='emDasfDFFmesaP8vHn8FaqOLkMSR0WhOJuglKgH85sevT')

user.GetUserTimeline(screen_name='twosetviolin', max_id=1044890036043431936)
