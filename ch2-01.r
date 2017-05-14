library(lars)
library(bayesm)
data(tuna)

x <- as.matrix(cbind(tuna[,16:22], tuna[,9:15], log(tuna[,30]))) #説明変数
y <- log(tuna[,2]) # Star Kist6オンスサイズの売り上げ
fit <- lars(x, y, type='lasso') # lasso推定量
lambda <- fit$lambda #使用された正則化パラーメータの値
beta <- fit$beta #推定された回帰係数の値
print(fit$beta)
print(lambda)

p <- ncol(x)
range.lam <- c(min(lambda), max(lambda))
range.beta <- c(min(beta), max(beta))
par(cex.lab=1.2)
par(cex.axis=1.2)
plot(range.lam, range.beta, xlab=expression(lambda), ylab='Estimated Coefficients', type='n')
for(i in 1:p) {lines(lambda, beta[-1, i], pch=1, cex=0.5, type='p')}
for(i in 1:p) {lines(lambda, beta[-1, i], lwd=2, lty=i, col=i)}