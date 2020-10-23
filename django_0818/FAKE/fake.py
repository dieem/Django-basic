from faker import Faker

# 가짜 Faker 객체 생성
myfake = Faker()
# 한국어로 된 객체 생성
# myfake = Faker('ko_KR')

# 같은 seed 사용 -> 같은 결과 출력
Faker.seed(1)

print(myfake.name()) 
print(myfake.address())
print(myfake.text()) 
print(myfake.sentence())
print(myfake.random_number())