def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
kwargs(name='saikiran', qualification='unemployed')
# format in nothing but string interpolation
# kwargs: key word arguments