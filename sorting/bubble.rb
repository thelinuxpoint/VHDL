def bubbleSort(arr)

	for i in 0..(arr.length-1)
		for j in 0..(arr.length-2-i)
			if arr[j] > arr[j+1]
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
			end
		end
	end
end

arr = gets.split(" ").map(&:to_i)
bubbleSort(arr)
p arr