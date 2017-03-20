from sklearn.linear_model import LinearRegression
slr = LinearRegression()

slr.fit(X,y)
print('Slope: %.3f' % slr.coef_[0])
print('intercept: %.3f' % slr.intercept_)
