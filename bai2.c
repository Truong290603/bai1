#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Hàm kiểm tra xem một số có phải là số chính phương hay không
bool is_perfect_square(int num) {
    // Lấy căn bậc hai của số
    int sqrt_num = (int)sqrt(num);
    // Kiểm tra xem căn bậc hai của số có phải là số nguyên hay không
    return (sqrt_num * sqrt_num == num);
}

// Hàm đếm và in ra các số chính phương nhỏ hơn n
int count_and_print_perfect_squares(int n) {
    printf("Cac so chinh phuong nho hon %d la:\n", n);
    int count = 0; // Biến đếm số lượng số chính phương

    // Duyệt từ 1 đến n-1 để tìm các số chính phương
    for (int i = 1; i < n; i++) {
        if (is_perfect_square(i)) { // Kiểm tra nếu là số chính phương
            printf("%d ", i); // In ra số chính phương
            count++; // Tăng biến đếm
        }
    }
    printf("\n");
    return count; // Trả về tổng số lượng số chính phương
}

int main() {
    int n;

    // Yêu cầu người dùng nhập số nguyên dương
    printf("Nhap mot so nguyen duong:\n ");
    scanf("%d", &n);

    // Kiểm tra nếu số nhập vào không hợp lệ
    if (n <= 0) {
        printf("Vui long nhap so nguyen duong.\n");
    } else {
        // Đếm và in các số chính phương nhỏ hơn n
        int count = count_and_print_perfect_squares(n);
        printf("Tong cong co %d so chinh phuong nho hon %d.\n", count, n);
    }

    return 0;
}
