A=zeros(5);
for i=1:5
    for j=1:5
        A(i,j)=(i-1)*5+j;
    end
end
sum(sum(A))
sum(diag(A))
sum(diag(A(1:end,end:-1:1)))
