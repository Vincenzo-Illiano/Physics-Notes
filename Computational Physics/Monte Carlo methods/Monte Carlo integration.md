In this note we will describe a method known as **Monte Carlo integration**, a method that uses Monte Carlo simulations in order to perform numerical integration. this is particularly useful to perform numerical integration of integrals in many dimensions.

## 1D integrals

For simplicity, we will first introduce the method with a one dimensional integral 
$$
I = \int_{a}^{b}f(x)dx.
$$
Let ${}\langle f(x) \rangle{}$ be the expectation value of ${}f{}$ when ${}x{}$ is uniformly distributed between ${}a{}$ and ${}b{}$. This is by definition 
$$
\langle f \rangle  = \int_{-\infty}^{\infty}f(x)p(x)dx = \frac{1}{b-a}\int_{a}^{b}f(x)dx.
$$
Therefore 
$$
I = (b-a)\langle f \rangle. \tag 1
$$
Using Monte Carlo methods we can estimate ${}\langle f \rangle{}$ using
$$
\bar{f} = \frac{1}{N}\sum_{i=1}^{N}f_{i},
$$
Where ${}f_{i}= f(x_{i}){}$ and the ${}x_{i}{}$ are sampled from a uniform distribution. Then we can use (1) to approximate ${}I{}$. This is the main idea of Monte Carlo integration.

To estimate the error of this method, we must calculate the variance of the estimator
$$
\hat{I} = (b-a)\bar{f},
$$
${}\sigma_{\hat{I}}^{2}{}$. This is given by 
$$
\sigma_{\bar{I}}^{2} = (b-a)^{2} \sigma_{\bar{f}}^{2} \approx (b-a)^2 \frac{S_{f}^{2}}{N},
$$
where ${}S_{f}^{2}{}$ is the sample variance of ${}f{}$
$$
S_{f}^{2} = \frac{1}{N-1}\sum_{i=1}^{N}(f_{i}-\bar{f})^{2},
$$
which tends to ${}\sigma_{f}^{2}{}$ as ${}N{}$ tends to infinity, and we are assuming that the samples ${}f_{i}{}$ are indipendent. 

Overall we have that:
$$
\int_{a}^{b} f(x)dx \approx \frac{b-a}{N} \sum_{i=1}^{N}f_{i} \pm \frac{b-a}{(N-1)\sqrt{ N }}\sum_{i=1}^{N}(f_{i}-\bar{f})^{2}. \tag 2
$$

## Higher dimensions

Eq. (2) can be generalized to any number of dimension, and for this reason Monte Carlo integration is particularly useful.

Let 
$$
I = \int_{a_{1}}^{b_{1}}dx_{1} \int_{a_{2}}^{b_{2}}dx_{2} \dots \int_{a_{n}}^{b_{n}}dx_{n}f(x_{1}, x_{2}, \dots, x_{n})= \int_{V}f(\vec{x})d \vec{x}.
$$
In the same way as we showed in one dimension, we have that 
$$
I = V \langle f(\vec{x}) \rangle ,
$$
where ${}\vec{x}{}$ is uniformly distributed in the volume ${}V{}$ instead of the length ${}b-a{}$; and, in the same way as we did in one dimension, we can compute ${}\langle f(\vec{x}) \rangle{}$ with Monte Carlo methods, sampling ${}\vec{x}{}$ from the volume ${}V{}$. Just like in one dimension, we thus have that 
$$
\boxed{I \approx \frac{V}{N}\sum_{i=1}^{N}f_{i} \pm \frac{VS_{f}}{\sqrt{ N }} }\tag 3
$$
which is the same as eq. (2), but generalized in any number of dimensions.

The error scales as ${}O(1 / N^{1 / 2}){}$, where ${}N{}$ is the number of samples. Notably, this is the same regardless of the number of dimensions in which we perform the integration. We can thus perform 10 dimensional integration with the same error as we would perform 1 dimensional integration! 
In addition, if the variance in the ${}f{}$ variable is small, then the error on the integration is small as well. For this reason, Monte Carlo integration is particularly effective for slow varying functions.

We can recognize when it is useful to use Monte Carlo integration by comparing it with the trapezoidal rule with stepsize ${}h{}$. This has a global error ${}O(h^{2}){}$. In order to compare it with Monte Carlo integration, it's convenient to write ${}h{}$ in terms of the amount of points ${}N{}$ that we compute. This can be more easily compared to the ${}N{}$ in Monte Carlo integration. In particular, we have that 
$$
N = N_{x_{1}}N_{x_{2}} \dots N_{x_{d}} \approx \left( \frac{1}{h} \right)^{d},
$$
where ${}d{}$ is the number of dimensions and ${}N_{x_{i}}{}$ is the number of points computed along the ${}x_{i}{}$ axis. Overall, the trapezoidal rule has error 
$$
O\left( \frac{1}{N^{2 / d}} \right),
$$
in comparison to the error ${}1 / N^{1 / 2}{}$ of Monte Carlo integration. This shows that Monte Carlo integration is preferable over trapezoidal integration when ${}d > 4.{}$ 

In general, compared to a method with global error ${}O(h^k){}$, MC integration is preferred when ${}d>2k{}$. 

## Importance sampling

Consider a function ${}f(x){}$ which is strongly peaked in a small part of the domain ${}[a, b]{}$. In such a case, sampling ${}x_{i}{}$ from a uniform distribution between ${}a{}$ and ${}b{}$ is particularly inefficient, as it severely underestimates ${}\sigma_{f}{}$, unless coincidentally some samples happen to hit the peak region. 

It's therefore convenient to sample ${}x{}$ from a different pdf ${}q(x) \neq f(x){}$. Then 
$$
I = \int_{a}^{b}f(x)dx = \int_{a}^{b} \frac{f(x)}{q(x)}q(x)dx = \int_{a}^{b}w(x)q(x)dx,
$$
where ${}w(x){}$ is the ratio between ${}f{}$ and ${}q{}$. Therefore 
$$
I = \langle w(x) \rangle_{q(x)},
$$
Where ${}x{}$ is sampled from ${}q(x){}$. Doing the same calculations as we did previously for MC integration, we thus get
$$
I \approx \frac{1}{N}\sum_{i=1}^{N}w_{i} \pm \frac{S_{w}}{\sqrt{ N }}
$$
This method is known as **importance sampling**. If we choose ${}q(x){}$ to be uniform, than it reduces to the "vanilla" Monte Carlo integration. On the other hand, choosing ${}q(x){}$ peaked similarly as ${}f(x){}$ can greatly reduce ${}S_{w}{}$ and thus reduce the total error. Similarly to ordinary MC integration, this can be generalized to any dimension.