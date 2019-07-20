import tensorflow as tf
xData = [1, 2, 3, 4, 5, 6, 7]
yData = [25000, 55000, 75000, 110000, 128000, 155000, 180000]
W = tf.Variable(tf.random.uniform([1], -100, 100)) # -100부터 100까지 랜덤한 값을 가진다
b = tf.Variable(tf.random.uniform([1], -100, 100))
X = tf.compat.v1.placeholder(tf.float32)
Y = tf.compat.v1.placeholder(tf.float32)
H = W * X + b
cost = tf.reduce_mean(tf.square(H - Y)) #reduce mean은 평균값을 의미한다
a = tf.Variable(0.01) #경사하강에서 얼나 경사하강을 할지 정해준다. 이값이 커지면 부정확해진다
optimizer = tf.compat.v1.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost) #값을 최소화 하는 방향으로 설정
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)
#학습을 시키는 파트
for i in range(5001):
    sess.run(train, feed_dict = {X: xData, Y: yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict = {X: xData, Y: yData}),sess.run(W),sess.run(b))
# x의 8번째 값의 예측한 값을 출력한다
print(sess.run(H, feed_dict={X: [8]}))
      
