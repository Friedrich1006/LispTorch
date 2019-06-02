from lt_parser import *

# torch.zeros(input.size(), dtype=input.dtype, layout=input.layout, device=input.device).
# torch.ones(input.size(), dtype=input.dtype, layout=input.layout, device=input.device)


my_list = [
	'torch.is_tensor(obj)',
	'torch.numel(input)',
	'torch.tensor(data, dtype=None, device=None, requires_grad=False, pin_memory=False)',
	'torch.as_tensor(data, dtype=None, device=None)',
	'torch.from_numpy(ndarray)',
	'torch.zeros(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.ones(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',	
	'torch.arange(start=0, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.range(start=0, end, step=1, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.eye(n, m=None, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.empty(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False, pin_memory=False)',
	'torch.full(size, fill_value, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.cat(tensors, dim=0, out=None)',
	'torch.chunk(tensor, chunks, dim=0)',
	'torch.gather(input, dim, index, out=None, sparse_grad=False)',
	'torch.index_select(input, dim, index, out=None)',
	'torch.masked_select(input, mask, out=None)',
	'torch.narrow(input, dimension, start, length)',
	'torch.nonzero(input, out=None)',
	'torch.reshape(input, shape)',
	'torch.split(tensor, split_size_or_sections, dim=0)',
	'torch.squeeze(input, dim=None, out=None)',
	'torch.stack(seq, dim=0, out=None)',
	'torch.t(input)',
	'torch.take(input, indices)',
	'torch.transpose(input, dim0, dim1)',
	'torch.unbind(tensor, dim=0)',
	'torch.unsqueeze(input, dim, out=None)',
	'torch.where(condition, x, y)',
	'torch.manual_seed(seed)',
	'torch.initial_seed()',
	'torch.normal(mean, std=1.0, out=None)',
	'torch.rand(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.randint(low=0, high, size, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.randn(*sizes, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.get_num_threads()',
	'torch.set_num_threads(int)',
	'torch.abs(input, out=None)',
	'torch.acos(input, out=None)',
	'torch.add(input, value, out=None)',
	'torch.asin(input, out=None)',
	'torch.atan(input, out=None)',
	'torch.atan2(input1, input2, out=None)',
	'torch.ceil(input, out=None)',
	'torch.clamp(input, min, max, out=None)',
	'torch.cos(input, out=None)',
	'torch.cosh(input, out=None)',
	'torch.div(input, value, out=None)',
	'torch.digamma(input, out=None)',
	'torch.erf(tensor, out=None)',
	'torch.erfc(input, out=None)',
	'torch.erfinv(input, out=None)',
	'torch.exp(input, out=None)',
	'torch.expm1(input, out=None)',
	'torch.floor(input, out=None)',
	'torch.fmod(input, divisor, out=None)',
	'torch.frac(input, out=None)',
	'torch.log(input, out=None)',
	'torch.log10(input, out=None)',
	'torch.log1p(input, out=None)',
	'torch.log2(input, out=None)',
	'torch.mul(input, value, out=None)',
	'torch.neg(input, out=None)',
	'torch.pow(input, exponent, out=None)',
	'torch.reciprocal(input, out=None)',
	'torch.remainder(input, divisor, out=None)',
	'torch.round(input, out=None)',
	'torch.rsqrt(input, out=None)',
	'torch.sigmoid(input, out=None)',
	'torch.sign(input, out=None)',
	'torch.sin(input, out=None)',
	'torch.sinh(input, out=None)',
	'torch.sqrt(input, out=None)',
	'torch.tan(input, out=None)',
	'torch.tanh(input, out=None)',
	'torch.trunc(input, out=None)',
	'torch.argmax(input, dim, keepdim=False)',
	'torch.argmin(input, dim, keepdim=False, out=None)',
	'torch.cumprod(input, dim, out=None, dtype=None)',
	'torch.cumsum(input, dim, out=None, dtype=None)',
	'torch.dist(input, other, p=2)',
	'torch.logsumexp(input, dim, keepdim=False, out=None)',
	'torch.mean(input, dim, keepdim=False, out=None)',
	'torch.median(input, dim=-1, keepdim=False, values=None, indices=None)',
	'torch.mode(input, dim=-1, keepdim=False, values=None, indices=None)',
	'torch.norm(input, p="fro", dim=None, keepdim=False, out=None, dtype=None)',
	'torch.prod(input, dim, keepdim=False, dtype=None)',
	'torch.std(input, dim, keepdim=False, unbiased=True, out=None)',
	'torch.sum(input, dim, keepdim=False, dtype=None)',
	'torch.unique(input, sorted=True, return_inverse=False, return_counts=False, dim=None)',
	'torch.unique_consecutive(input, return_inverse=False, return_counts=False, dim=None)',
	'torch.var(input, dim, keepdim=False, unbiased=True, out=None)',
	'torch.argsort(input, dim=-1, descending=False, out=None)',
	'torch.allclose(self, other, rtol=1e-05, atol=1e-08, equal_nan=False)',
	'torch.equal(tensor1, tensor2)',
	'torch.ge(input, other, out=None)',
	'torch.gt(input, other, out=None)',
	'torch.isfinite(tensor)',
	'torch.isinf(tensor)',
	'torch.isnan(tensor)',
	'torch.le(input, other, out=None)',
	'torch.lt(input, other, out=None)',
	'torch.max(input, dim, keepdim=False, out=None)',
	'torch.min(input, dim, keepdim=False, out=None)',
	'torch.ne(input, other, out=None)',
	'torch.sort(input, dim=-1, descending=False, out=None)',
	'torch.topk(input, k, dim=None, largest=True, sorted=True, out=None)',
	'torch.fft(input, signal_ndim, normalized=False)',
	'torch.ifft(input, signal_ndim, normalized=False)',
	'torch.rfft(input, signal_ndim, normalized=False, onesided=True)',
	'torch.irfft(input, signal_ndim, normalized=False, onesided=True, signal_sizes=None)',
	'torch.stft(input, n_fft, hop_length=None, win_length=None, window=None, center=True, pad_mode="reflect", normalized=False, onesided=True)',
	'torch.bartlett_window(window_length, periodic=True, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.blackman_window(window_length, periodic=True, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.hamming_window(window_length, periodic=True, alpha=0.54, beta=0.46, dtype=None, layout=torch.strided, device=None, requires_grad=False)',
	'torch.cross(input, other, dim=-1, out=None)',
	'torch.diag(input, diagonal=0, out=None)',
	'torch.einsum(equation, *operands)',
	'torch.flatten(input, start_dim=0, end_dim=-1)',
	'torch.flip(input, dims)',
	'torch.tensordot(a, b, dims=2)',
	'torch.trace(input)',
	'torch.addbmm(beta=1, mat, alpha=1, batch1, batch2, out=None)',
	'torch.addmm(beta=1, mat, alpha=1, mat1, mat2, out=None)',
	'torch.bmm(batch1, batch2, out=None)',
	'torch.dot(tensor1, tensor2)',
	'torch.eig(a, eigenvectors=False, out=None)',
	'torch.geqrf(input, out=None)',	
	'torch.inverse(input, out=None)',
	'torch.det(A)',
	'torch.logdet(A)',
	'torch.matmul(tensor1, tensor2, out=None)',
	'torch.mm(mat1, mat2, out=None)',
	'torch.mv(mat, vec, out=None)',
	
]


# (define t_xxx
#	(lambda (x y:blabla z:blabla)
#		(_torch_xxx x y z)))

def convert(string, fout):
	tokens = tokenize(string)
	name = tokens[0].replace('torch.', '_torch_').replace('.', '_')

	if '*' in string:
		args = []
		tokens = [token.replace(',', '') for token in tokens]
		for token in tokens[2:-1]:
			if '=' in token:
				args.append(token.split('=')[0])
			else:
				args.append(token)
		double_args = [arg+'='+arg for arg in args[1:]]
		fout.write("    '%s': lambda %s: %s(%s),\n" % (name, ', '.join(args).replace('*', ''), tokens[0], args[0] + ', ' + ', '.join(double_args)))
	else:
		args = []
		tokens = [token.replace(',', '') for token in tokens]
		for token in tokens[2:-1]:
			if '=' in token:
				args.append(token.split('=')[0])
			else:
				args.append(token)
		double_args = [arg+'='+arg for arg in args]
		fout.write("    '%s': lambda %s: %s(%s),\n" % (name, ', '.join(args), tokens[0], ', '.join(double_args)))

def lisp_func(string, fout):
	raw_tokens = tokenize(string)
	name = raw_tokens[0].replace('torch.', '_torch_').replace('.', '_')
	lisp_name = raw_tokens[0].replace('torch.', 't_').replace('.', '_')

	tokens = []

	for token in raw_tokens:
		token = token.replace('torch.', 't_')
		token = token.replace('.', '_')
		token = token.replace('=', ':')
		token = token.replace('False', '#f')
		token = token.replace('True', '#t')
		token = token.replace('None', '#n')
		token = token.replace(',', '')
		tokens.append(token)

	func = '(define %s (lambda (' % lisp_name

	func += ' '.join(tokens[2:-1]) + ') (' + name

	args = []

	for token in tokens[2:-1]:
		if ':' in token:
			args.append(token.split(':')[0])
		else:
			args.append(token)

	func += ' ' + ' '.join(args) + ')))'

	fout.write(func + '\n')


if __name__ == '__main__':
	with open('lt_torch.py', 'w') as fout:
		fout.write('import torch\n')
		fout.write('torch_env = {' + '\n')
		fout.write("    't_view': lambda tensor, _list: tensor.view(*_list)," + '\n')
		fout.write("    't_size': lambda tensor: tensor.size()," + '\n')
		fout.write("    't_strided': torch.strided," + '\n')
		for func in my_list:
			convert(func, fout)
		fout.write('}')


	with open('torch.lisp', 'w') as fout:
		for func in my_list:
			lisp_func(func, fout)