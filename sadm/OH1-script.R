# set the seed of the random number generator -- useful for reproducibility
set.seed(0)

"
Example 1: generate a set of uncorrelated predictors and build a multiple 
linear regression model on the data. We expect to not reject any of the 
statistical tests, i.e. F-test and t-test
"

# number of samples
n <- 1000
# number of predictors
p <- 5
# generate an array of real numbers from standard normal
M <- rnorm(n*p, mean=0, sd=1)
# create a n-by-p matrix with the sampled points
M <- matrix(M, nrow=n, ncol=p)
# create a data frame from the data matrix created above
df <- data.frame(M)
# estimate the parameters of a linear model to predict the first column in 
# terms of all the other columns in the matrix
mylm <- lm(X1 ~ ., data=df)
# print the results of the linear model
summary(mylm)
# we can plot the normalized histogram of the residuals...
res <- mylm$residuals
bins <- seq(-5, +5, length.out=40)
hist(res, breaks=bins, xlab="residual", ylab="frequency", 
     main="normalized histogram of residuals", prob=TRUE)
# ...and can overlay it with the plot of a gaussian distribution 
mu <- mean(res)
sd <- sd(res)
x <- seq(-5, +5, length.out=100)
y <- dnorm(x, mean=mu, sd=sd)
lines(x, y, col="red", lwd=3.0)

"
Example 2: generate a set of data points following a given mean and covariance
"

# Option 1
npoints <- 1000
theta <- -pi/4
mu1 <- 0.0
sd1 <- 1.0
mu2 <- 0.0
sd2 <- 4.0
eps1 <- rnorm(npoints)
eps2 <- rnorm(npoints)
X1 <- mu1 + cos(theta) * sd1 * eps1 - sin(theta) * sd2 * eps2
X2 <- mu2 + sin(theta) * sd1 * eps1 + cos(theta) * sd2 * eps2
df <- data.frame(cbind(X1, X2))
plot(df, xlim=c(-10, +10), ylim=c(-10, +10))

# Option 2
eps <- rbind(eps1, eps2)
Q <- cbind(c(cos(theta), sin(theta)), c(-sin(theta), cos(theta)))
L <- cbind(c(sd1, 0.0), c(0.0, sd2))
X <- t(Q %*% L %*% eps) # matrix multiplication in R is done via %*%
df <- data.frame(X)
plot(df, xlim=c(-10, +10), ylim=c(-10, +10))

"
Example 3: loading a dataset and doing some initial analysis
"

df <- read.table("prostate.data") # load a dataset that had been saved with R
df <- df[1:(ncol(df) - 1)] # discard last column from the data frame
pairs(df) # scatterplot of each pair of predictors

# make the categorical variables be treated as factors
df$svi <- factor(df$svi)
df$gleason <- factor(df$gleason)

# run a multiple linear regression using all predictors
mylm <- lm(lcavol ~ ., data=df)

