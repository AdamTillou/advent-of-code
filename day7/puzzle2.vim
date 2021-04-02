function! g:ContainedBags(color)
	silent! norm! gg"ayG
	
	let matches = functions#GetMatches(@a, "\n" . '\zs' . a:color . "[^\n]*")
	if len(matches) == 0 || stridx(matches[0], 'no other bags') != -1
		return 1
	endif
	
	let line = substitute(matches[0], '^\l\+ \l\+ bags contain ', '', '')
	let bags = split(line, ',')
	
	let bag_sum = 1
	for q in bags
		let bag_count = functions#GetMatches(q, '\d')[0]
		let bag_color = functions#GetMatches(q, '\d \zs\l\+ \l\+\ze bag')[0]
		let bags_inside = g:ContainedBags(bag_color)
		let bag_sum += bag_count * bags_inside
	endfor
	
	return bag_sum
endfunction
