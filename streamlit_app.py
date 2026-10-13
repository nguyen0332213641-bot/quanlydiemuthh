import streamlit as st

# Cấu hình giao diện trang web rộng rãi
st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN - UTH", layout="wide")

# Đoạn mã HTML/CSS/JS hoàn chỉnh của bạn được đưa thẳng vào đây
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QUẢN LÝ ĐIỂM SINH VIÊN - UTH</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Merriweather:wght@700;900&display=swap" rel="stylesheet">
    
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f0f4f8;
            color: #1e293b;
            margin: 0;
            padding: 1rem;
        }
        .uth-font {
            font-family: 'Merriweather', serif;
        }
        .card-shadow {
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        }
        .table-wrapper::-webkit-scrollbar {
            height: 8px;
        }
        .table-wrapper::-webkit-scrollbar-thumb {
            background: #cbd5e1;
            border-radius: 4px;
        }
        .table-wrapper::-webkit-scrollbar-track {
            background: #f1f5f9;
        }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <div class="max-w-7xl mx-auto w-full space-y-6 flex-grow">
        
        <!-- Header & Logo -->
        <header class="bg-white rounded-2xl p-6 md:p-8 card-shadow flex flex-col md:flex-row items-center md:items-start justify-between gap-6 border-t-4 border-blue-800">
            <div class="flex flex-col items-center justify-center shrink-0">
                <div class="text-5xl md:text-6xl font-black uth-font tracking-tight" style="color: #008080; text-shadow: 1px 1px 0 #f59e0b, -1px -1px 0 #f59e0b, 1px -1px 0 #f59e0b, -1px 1px 0 #f59e0b, 2px 2px 4px rgba(0,0,0,0.2);">
                    UTH
                </div>
                <div class="text-center mt-2 leading-tight">
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">UNIVERSITY</div>
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">OF TRANSPORT</div>
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">HOCHIMINH CITY</div>
                </div>
            </div>
            
            <div class="flex-grow flex items-center md:justify-end text-center md:text-right w-full md:w-auto h-full">
                <div>
                    <h1 class="text-2xl md:text-3xl lg:text-4xl font-bold text-blue-900 tracking-tight">QUẢN LÝ ĐIỂM SINH VIÊN</h1>
                    <p class="text-slate-500 mt-2 font-medium">Khoa Công nghệ Thông tin - Học kỳ I (2026 - 2027)</p>
                </div>
            </div>
        </header>

        <!-- Thống kê -->
        <section>
            <h2 class="text-lg font-bold text-slate-700 mb-3 flex items-center gap-2 uppercase tracking-wide">
                Thống kê tổng quan
            </h2>
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4" id="statsContainer"></div>
        </section>

        <!-- Bảng điểm chi tiết -->
        <section class="bg-white rounded-2xl p-6 card-shadow border border-slate-100">
            <h2 class="text-lg font-bold text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wide">
                1. Bảng điểm chi tiết
            </h2>
            <div class="table-wrapper overflow-x-auto rounded-xl border border-slate-200">
                <table class="w-full text-left border-collapse whitespace-nowrap">
                    <thead>
                        <tr class="bg-slate-50 text-slate-600 text-sm tracking-wide">
                            <th class="p-3 border-b text-center font-semibold w-16">STT</th>
                            <th class="p-3 border-b font-semibold">Họ và tên</th>
                            <th class="p-3 border-b text-center font-semibold">Chuyên cần <span class="text-xs text-slate-400 font-normal">(20%)</span></th>
                            <th class="p-3 border-b text-center font-semibold">Giữa kỳ <span class="text-xs text-slate-400 font-normal">(30%)</span></th>
                            <th class="p-3 border-b text-center font-semibold">Cuối kỳ <span class="text-xs text-slate-400 font-normal">(50%)</span></th>
                            <th class="p-3 border-b text-center font-bold text-blue-800">Tổng kết</th>
                            <th class="p-3 border-b text-center font-semibold">Xếp loại</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" class="divide-y divide-slate-100 text-sm"></tbody>
                </table>
            </div>
        </section>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <!-- Tra cứu sinh viên -->
            <section class="lg:col-span-1 bg-white rounded-2xl p-6 card-shadow border border-slate-100 flex flex-col">
                <h2 class="text-lg font-bold text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wide">
                    3. Tra cứu sinh viên
                </h2>
                
                <div class="mb-5 relative">
                    <label for="studentSelect" class="block text-sm font-medium text-slate-600 mb-1">Chọn hoặc tìm sinh viên:</label>
                    <select id="studentSelect" class="w-full bg-slate-50 border border-slate-300 text-slate-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5 cursor-pointer outline-none">
                        <option value="" disabled selected>-- Chọn sinh viên --</option>
                    </select>
                </div>

                <div id="studentDetailCard" class="hidden flex-grow bg-gradient-to-br from-blue-50 to-slate-50 rounded-xl p-5 border border-blue-100 relative overflow-hidden">
                    <div class="absolute -right-6 -top-6 w-24 h-24 bg-blue-100 rounded-full opacity-50"></div>
                    
                    <div class="relative z-10">
                        <div class="flex items-center gap-3 mb-4 border-b border-blue-200 pb-3">
                            <div class="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center font-bold text-lg shadow-md" id="detailAvatar">A</div>
                            <div>
                                <h3 id="detailName" class="text-lg font-bold text-blue-900 leading-tight">Tên Sinh Viên</h3>
                                <p class="text-xs text-blue-600 font-medium">Sinh viên CNTT</p>
                            </div>
                        </div>
                        
                        <div class="space-y-2.5 text-sm">
                            <div class="flex justify-between items-center bg-white p-2 rounded border border-slate-100">
                                <span class="text-slate-500">Chuyên cần:</span>
                                <span id="detailCC" class="font-bold text-slate-800">0</span>
                            </div>
                            <div class="flex justify-between items-center bg-white p-2 rounded border border-slate-100">
                                <span class="text-slate-500">Giữa kỳ:</span>
                                <span id="detailGK" class="font-bold text-slate-800">0</span>
                            </div>
                            <div class="flex justify-between items-center bg-white p-2 rounded border border-slate-100">
                                <span class="text-slate-500">Cuối kỳ:</span>
                                <span id="detailCK" class="font-bold text-slate-800">0</span>
                            </div>
                            
                            <div class="mt-4 pt-3 flex justify-between items-end">
                                <div>
                                    <span class="block text-xs text-slate-500 mb-1">Xếp loại</span>
                                    <span id="detailXL" class="font-bold px-3 py-1 rounded-full text-xs">Loại</span>
                                </div>
                                <div class="text-right">
                                    <span class="block text-xs text-slate-500 mb-1">Tổng kết</span>
                                    <span id="detailTK" class="text-3xl font-black text-blue-700 leading-none">0.0</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Biểu đồ cột -->
            <section class="lg:col-span-2 bg-white rounded-2xl p-6 card-shadow border border-slate-100">
                <h2 class="text-lg font-bold text-slate-700 mb-4 flex items-center gap-2 uppercase tracking-wide">
                    4. Biểu đồ cột: Điểm tổng kết
                </h2>
                <div class="w-full h-[320px] relative">
                    <canvas id="gradeChart"></canvas>
                </div>
            </section>
        </div>

    </div>

    <!-- Footer -->
    <footer class="mt-8 text-center text-slate-500 text-sm pb-6 flex flex-col items-center gap-2">
        <p>Bản quyền © Nguyễn Ngọc Nguyên - UTH</p>
        <div class="mt-2 font-medium text-blue-900 bg-blue-50/80 inline-block px-5 py-2.5 rounded-xl border border-blue-200 shadow-sm">
            Sinh viên thực hiện: <b class="text-black-700 uppercase">Nguyễn Ngọc Nguyên</b> <span class="mx-2 text-blue-300">|</span> MSSV: <b class="text-black-700">060208009198</b>
        </div>
    </footer>

    <script>
        const data = [
            { id: 1, name: 'An', cc: 8, gk: 7, ck: 8 },
            { id: 2, name: 'Tiến', cc: 9, gk: 8, ck: 8 },
            { id: 3, name: 'Tiền', cc: 3, gk: 6, ck: 3 },
            { id: 4, name: 'Hào', cc: 10, gk: 3, ck: 6 },
            { id: 5, name: 'Dũng', cc: 8, gk: 7, ck: 7 },
            { id: 6, name: 'Đô', cc: 6, gk: 5, ck: 6 },
            { id: 7, name: 'Tuấn', cc: 9, gk: 8, ck: 8 },
            { id: 8, name: 'Thành', cc: 8, gk: 7, ck: 6 },
            { id: 9, name: 'Thư', cc: 7, gk: 7, ck: 8 },
            { id: 10, name: 'Trung', cc: 10, gk: 9, ck: 9 }
        ];

        const students = data.map(student => {
            let tongKet = (student.cc * 0.2) + (student.gk * 0.3) + (student.ck * 0.5);
            tongKet = Math.round(tongKet * 10) / 10;
            
            let xepLoai = '';
            let badgeClass = '';
            
            if (tongKet >= 8.5) {
                xepLoai = 'Giỏi';
                badgeClass = 'bg-green-100 text-green-700 border-green-200';
            } else if (tongKet >= 7.0) {
                xepLoai = 'Khá';
                badgeClass = 'bg-blue-100 text-blue-700 border-blue-200';
            } else if (tongKet >= 5.0) {
                xepLoai = 'Trung bình';
                badgeClass = 'bg-yellow-100 text-yellow-700 border-yellow-200';
            } else {
                xepLoai = 'Yếu';
                badgeClass = 'bg-red-100 text-red-700 border-red-200';
            }

            return { ...student, tongKet, xepLoai, badgeClass };
        });

        const tableBody = document.getElementById('tableBody');
        students.forEach(s => {
            const row = document.createElement('tr');
            row.className = "hover:bg-blue-50 transition-colors duration-150";
            row.innerHTML = `
                <td class="p-3 border-b text-center text-slate-500">${s.id}</td>
                <td class="p-3 border-b font-medium text-slate-800">${s.name}</td>
                <td class="p-3 border-b text-center text-slate-600">${s.cc}</td>
                <td class="p-3 border-b text-center text-slate-600">${s.gk}</td>
                <td class="p-3 border-b text-center text-slate-600">${s.ck}</td>
                <td class="p-3 border-b text-center font-bold text-blue-700 bg-blue-50/50">${s.tongKet}</td>
                <td class="p-3 border-b text-center">
                    <span class="px-2.5 py-1 rounded-md text-xs font-semibold border ${s.badgeClass}">
                        ${s.xepLoai}
                    </span>
                </td>
            `;
            tableBody.appendChild(row);
        });

        const allScores = students.map(s => s.tongKet);
        const avgScore = (allScores.reduce((a, b) => a + b, 0) / students.length).toFixed(2);
        const maxScore = Math.max(...allScores);
        const minScore = Math.min(...allScores);
        const passCount = students.filter(s => s.tongKet >= 5.0).length;

        const statsHtml = `
            <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xl font-bold">Σ</div>
                <div>
                    <p class="text-sm text-slate-500 font-medium">Trung bình lớp</p>
                    <p class="text-2xl font-black text-slate-800">${avgScore}</p>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xl font-bold">↑</div>
                <div>
                    <p class="text-sm text-slate-500 font-medium">Điểm cao nhất</p>
                    <p class="text-2xl font-black text-slate-800">${maxScore}</p>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-red-100 text-red-500 flex items-center justify-center text-xl font-bold">↓</div>
                <div>
                    <p class="text-sm text-slate-500 font-medium">Điểm thấp nhất</p>
                    <p class="text-2xl font-black text-slate-800">${minScore}</p>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-slate-100 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-full bg-teal-100 text-teal-600 flex items-center justify-center text-xl font-bold">✓</div>
                <div>
                    <p class="text-sm text-slate-500 font-medium">Số sinh viên đạt</p>
                    <p class="text-2xl font-black text-slate-800">${passCount} <span class="text-sm font-normal text-slate-400">/ 10</span></p>
                </div>
            </div>
        `;
        document.getElementById('statsContainer').innerHTML = statsHtml;

        const studentSelect = document.getElementById('studentSelect');
        const detailCard = document.getElementById('studentDetailCard');
        
        students.forEach(s => {
            const option = document.createElement('option');
            option.value = s.id;
            option.textContent = `${s.id}. ${s.name}`;
            studentSelect.appendChild(option);
        });

        studentSelect.addEventListener('change', (e) => {
            const s = students.find(student => student.id == e.target.value);
            if (s) {
                document.getElementById('detailAvatar').textContent = s.name.charAt(0);
                document.getElementById('detailName').textContent = s.name;
                document.getElementById('detailCC').textContent = s.cc;
                document.getElementById('detailGK').textContent = s.gk;
                document.getElementById('detailCK').textContent = s.ck;
                document.getElementById('detailTK').textContent = s.tongKet;
                
                const detailXL = document.getElementById('detailXL');
                detailXL.textContent = s.xepLoai;
                detailXL.className = `font-bold px-3 py-1 rounded-full text-xs border ${s.badgeClass}`;
                
                detailCard.classList.remove('hidden');
            }
        });

        const ctx = document.getElementById('gradeChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: students.map(s => s.name),
                datasets: [{
                    label: 'Điểm Tổng Kết',
                    data: allScores,
                    backgroundColor: 'rgba(37, 99, 235, 0.85)',
                    hoverBackgroundColor: '#1d4ed8',
                    borderRadius: 6,
                    barPercentage: 0.6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#1e293b',
                        padding: 12,
                        callbacks: {
                            label: (context) => `Điểm: ${context.parsed.y}`
                        }
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 10,
                        grid: { color: '#f1f5f9', drawBorder: false },
                        ticks: { stepSize: 2 }
                    },
                    x: {
                        grid: { display: false, drawBorder: false },
                    }
                }
            }
        });
    </script>
</body>
</html>
"""

# Hiển thị lên web Streamlit với chiều cao thích hợp
st.components.v1.html(html_code, height=1150, scrolling=True)
