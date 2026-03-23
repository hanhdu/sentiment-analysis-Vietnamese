document.addEventListener('DOMContentLoaded', () => {
    const predictBtn = document.getElementById('predictBtn');
    const textInput = document.getElementById('textInput');
    const loadingBox = document.getElementById('loadingBox');
    const resultBox = document.getElementById('resultBox');
    const resultTableBody = document.getElementById('resultTableBody');
    const errorAlert = document.getElementById('errorAlert');
    const cleanTextDisplay = document.getElementById('cleanTextDisplay');

    predictBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        
        // Reset Giao diện
        errorAlert.classList.add('d-none');
        resultBox.classList.add('d-none');
        resultTableBody.innerHTML = '';
        
        if (!text) {
            showError("Vui lòng nhập bình luận trước khi dự đoán!");
            return;
        }

        // Bật Loading
        predictBtn.disabled = true;
        loadingBox.classList.remove('d-none');

        try {
            // Gọi API lên Backend
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Có lỗi xảy ra từ máy chủ.");
            }

            // Hiển thị text đã qua tiền xử lý
            cleanTextDisplay.textContent = `"${data.clean_text}"`;

            // Tìm mô hình có thời gian nhanh nhất (để highlight)
            const minTime = Math.min(...data.results.map(r => r.time_ms));

            // Render bảng kết quả
            data.results.forEach(item => {
                const isFastest = item.time_ms === minTime;
                const row = document.createElement('tr');
                
                // Highlight row nếu nhanh nhất
                if (isFastest) {
                    row.classList.add('fastest-row');
                }

                // Chỉnh màu Label
                let badgeClass = 'badge-trungtinh';
                let icon = '<i class="fas fa-meh"></i>';
                if (item.label === 'Tích cực') {
                    badgeClass = 'badge-tichcuc';
                    icon = '<i class="fas fa-smile-beam"></i>';
                } else if (item.label === 'Tiêu cực') {
                    badgeClass = 'badge-tieucuc';
                    icon = '<i class="fas fa-angry"></i>';
                }

                row.innerHTML = `
                    <td class="fw-bold text-dark">
                        ${item.model} 
                        ${isFastest ? '<span class="badge bg-warning text-dark ms-2"><i class="fas fa-bolt"></i> Nhanh nhất</span>' : ''}
                    </td>
                    <td><span class="badge rounded-pill px-3 py-2 ${badgeClass}">${icon} ${item.label}</span></td>
                    <td>
                        <div class="d-flex align-items-center">
                            <span class="me-2 fw-bold">${item.confidence}%</span>
                            <div class="progress flex-grow-1" style="height: 8px;">
                                <div class="progress-bar bg-primary" role="progressbar" style="width: ${item.confidence}%;"></div>
                            </div>
                        </div>
                    </td>
                    <td class="text-muted fw-semibold">${item.time_ms} ms</td>
                `;
                resultTableBody.appendChild(row);
            });

            // Tắt Loading, Hiển thị Kết quả
            loadingBox.classList.add('d-none');
            resultBox.classList.remove('d-none');

        } catch (error) {
            loadingBox.classList.add('d-none');
            showError(error.message);
        } finally {
            predictBtn.disabled = false;
        }
    });

    function showError(msg) {
        errorAlert.textContent = msg;
        errorAlert.classList.remove('d-none');
    }
});