import streamlit as st

st.set_page_config(page_title="QUẢN LÝ ĐIỂM SINH VIÊN - UTH", layout="wide")

html_code = """
<!-- DÁN TOÀN BỘ MÃ HTML Ở TRÊN VÀO ĐÂY -->
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QUẢN LÝ ĐIỂM SINH VIÊN - UTH</title>
    <!-- Tailwind CSS & Chart.js -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Merriweather:wght@700;900&display=swap" rel="stylesheet">
    
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; color: #0f172a; }
        .uth-font { font-family: 'Merriweather', serif; }
        .card-hover { transition: all 0.25s ease; }
        .card-hover:hover { transform: translateY(-3px); box-shadow: 0 12px 24px -6px rgba(15, 23, 42, 0.08); }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }
        .animate-fade-in { animation: fadeIn 0.3s ease-out forwards; }
        ::-webkit-scrollbar { height: 6px; width: 6px; }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-track { background: #f1f5f9; }
    </style>
</head>
<body class="min-h-screen flex flex-col p-4 md:p-6 lg:p-8">

    <div class="max-w-7xl mx-auto w-full space-y-6 flex-grow">
        
        <!-- Header chuẩn Logo UTH -->
        <header class="bg-white rounded-2xl p-6 md:p-8 border border-slate-200/80 shadow-sm flex flex-col md:flex-row items-center md:items-start justify-between gap-6 border-t-4 border-t-blue-700 relative overflow-hidden">
            <div class="absolute -right-16 -top-16 w-40 h-40 bg-blue-50 rounded-full blur-2xl pointer-events-none"></div>

            <div class="flex flex-col items-center justify-center shrink-0 relative z-10">
                <div class="text-5xl md:text-6xl font-black uth-font tracking-tight" style="color: #008080; text-shadow: 1px 1px 0 #f59e0b, -1px -1px 0 #f59e0b, 1px -1px 0 #f59e0b, -1px 1px 0 #f59e0b, 2px 2px 4px rgba(0,0,0,0.2);">
                    UTH
                </div>
                <div class="text-center mt-2 leading-tight">
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">UNIVERSITY</div>
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">OF TRANSPORT</div>
                    <div class="text-red-600 font-bold text-xs tracking-widest uppercase" style="font-family: 'Impact', sans-serif; letter-spacing: 0.1em; -webkit-text-stroke: 0.5px #f59e0b;">HOCHIMINH CITY</div>
                </div>
            </div>
            
            <div class="flex-grow flex flex-col md:items-end text-center md:text-right relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 bg-emerald-50 text-emerald-700 text-xs font-semibold rounded-full border border-emerald-200/80 mb-2">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                    Hệ thống Phân tích & Quản lý Học tập
                </div>
                <h1 class="text-2xl md:text-3xl lg:text-4xl font-extrabold text-slate-900 tracking-tight">QUẢN LÝ ĐIỂM SINH VIÊN</h1>
                <p class="text-slate-500 mt-1 text-sm font-medium">Trí tuệ nhân tạo và ứng dụng - Học kỳ I (2026 - 2027)</p>
            </div>
        </header>

        <!-- Thống kê tổng quan -->
        <section>
            <div class="flex items-center justify-between mb-3">
                <h2 class="text-xs font-bold text-slate-400 uppercase tracking-wider">Thống kê tổng quan</h2>
                <span class="text-xs text-blue-600 font-semibold bg-blue-50 px-2.5 py-0.5 rounded-full">Sĩ số: 10 SV</span>
            </div>
            <div class="grid grid-cols-2 lg:grid-cols-4 gap-4" id="statsContainer"></div>
        </section>

        <!-- Cảnh báo học tập -->
        <section class="bg-amber-50/60 border border-amber-200/80 rounded-2xl p-4 md:p-5 flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
            <div class="flex items-start gap-3">
                <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-xl shrink-0">⚠️</div>
                <div>
                    <h3 class="text-sm font-bold text-amber-900">Cảnh báo học tập & Nhận xét lớp học</h3>
                    <p class="text-xs text-amber-800/90 mt-0.5" id="insightText">Đang tải phân tích...</p>
                </div>
            </div>
            <div id="riskStudentsBadge" class="flex flex-wrap gap-1.5 shrink-0"></div>
        </section>

        <!-- Bảng điểm chi tiết -->
        <section class="bg-white rounded-2xl p-6 border border-slate-200/80 shadow-sm">
            <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-5">
                <h2 class="text-base font-bold text-slate-800 uppercase tracking-wide flex items-center gap-2">
                    <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> 1. Bảng điểm chi tiết
                </h2>

                <div class="flex flex-wrap items-center gap-3">
                    <div class="relative w-full sm:w-48">
                        <input type="text" id="searchInput" oninput="window.handleSearch()" placeholder="🔍 Tìm tên..." class="w-full bg-slate-50 border border-slate-200 text-slate-800 text-xs rounded-xl px-3 py-2 outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white transition-all">
                    </div>
                    <div class="flex items-center gap-1 bg-slate-100 p-1 rounded-xl text-xs font-semibold overflow-x-auto">
                        <button onclick="window.filterTable('All')" class="filter-btn active px-3 py-1.5 rounded-lg bg-white text-blue-700 shadow-sm transition-all">Tất cả</button>
                        <button onclick="window.filterTable('Giỏi')" class="filter-btn px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all">Giỏi</button>
                        <button onclick="window.filterTable('Khá')" class="filter-btn px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all">Khá</button>
                        <button onclick="window.filterTable('Trung bình')" class="filter-btn px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all">Trung bình</button>
                        <button onclick="window.filterTable('Yếu')" class="filter-btn px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition-all">Yếu</button>
                    </div>
                </div>
            </div>
            
            <div class="overflow-x-auto rounded-xl border border-slate-200">
                <table class="w-full text-left border-collapse whitespace-nowrap">
                    <thead>
                        <tr class="bg-slate-50/80 text-slate-600 text-xs font-bold uppercase tracking-wider border-b border-slate-200">
                            <th class="p-3.5 text-center w-16">STT</th>
                            <th class="p-3.5">Họ và tên</th>
                            <th class="p-3.5 text-center">Chuyên cần <span class="text-slate-400 font-normal">(20%)</span></th>
                            <th class="p-3.5 text-center">Giữa kỳ <span class="text-slate-400 font-normal">(30%)</span></th>
                            <th class="p-3.5 text-center">Cuối kỳ <span class="text-slate-400 font-normal">(50%)</span></th>
                            <th class="p-3.5 text-center text-blue-700 font-bold bg-blue-50/50 cursor-pointer hover:bg-blue-100/50 transition-colors" onclick="window.toggleSort()">
                                Tổng kết <span id="sortIcon">⇅</span>
                            </th>
                            <th class="p-3.5 text-center">Xếp loại</th>
                        </tr>
                    </thead>
                    <tbody id="tableBody" class="divide-y divide-slate-100 text-sm text-slate-700"></tbody>
                </table>
            </div>
        </section>

        <!-- KHU VỰC CÔNG CỤ: TRA CỨU SINH VIÊN & DỰ ĐOÁN ĐIỂM -->
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            
            <!-- TRA CỨU SINH VIÊN -->
            <section class="bg-white rounded-2xl p-6 border border-slate-200/80 shadow-sm flex flex-col justify-between">
                <div>
                    <h2 class="text-base font-bold text-slate-800 uppercase tracking-wide mb-4 flex items-center gap-2">
                        🔍 2. Tra cứu sinh viên
                    </h2>
                    
                    <div class="mb-4">
                        <label for="studentSelect" class="block text-xs font-semibold text-slate-500 mb-1.5 uppercase">Chọn sinh viên:</label>
                        <select id="studentSelect" onchange="window.handleSelectStudent()" class="w-full bg-slate-50 border border-slate-300 text-slate-800 text-xs rounded-xl p-3 focus:ring-2 focus:ring-blue-500 outline-none transition-all cursor-pointer font-medium">
                            <option value="" disabled selected>-- Chọn sinh viên để xem --</option>
                        </select>
                    </div>

                    <div id="studentDetailCard" class="hidden bg-slate-50/80 rounded-xl p-4 border border-slate-200/80 relative overflow-hidden flex flex-col justify-between animate-fade-in">
                        <div>
                            <div class="flex items-center gap-3 pb-3 mb-3 border-b border-slate-200">
                                <div class="w-10 h-10 rounded-xl bg-gradient-to-br from-blue-600 to-teal-500 text-white flex items-center justify-center font-bold text-base shadow-sm" id="detailAvatar">A</div>
                                <div>
                                    <h3 id="detailName" class="text-base font-bold text-slate-900 leading-tight">Tên Sinh Viên</h3>
                                    <p class="text-xs text-blue-600 font-medium">Kỹ thuật điện</p>
                                </div>
                            </div>
                            
                            <div class="space-y-2 text-xs">
                                <div class="flex justify-between items-center py-1 border-b border-slate-200/60">
                                    <span class="text-slate-500">Chuyên cần (20%):</span>
                                    <span id="detailCC" class="font-semibold text-slate-800">0</span>
                                </div>
                                <div class="flex justify-between items-center py-1 border-b border-slate-200/60">
                                    <span class="text-slate-500">Giữa kỳ (30%):</span>
                                    <span id="detailGK" class="font-semibold text-slate-800">0</span>
                                </div>
                                <div class="flex justify-between items-center py-1">
                                    <span class="text-slate-500">Cuối kỳ (50%):</span>
                                    <span id="detailCK" class="font-semibold text-slate-800">0</span>
                                </div>
                            </div>

                            <div class="mt-4 pt-3 border-t border-slate-200">
                                <div class="flex justify-between text-xs font-semibold text-slate-500 mb-1">
                                    <span>Thang điểm 10</span>
                                    <span id="progressText" class="text-blue-700">0%</span>
                                </div>
                                <div class="w-full bg-slate-200 rounded-full h-2 overflow-hidden">
                                    <div id="progressBar" class="bg-gradient-to-r from-blue-500 to-teal-400 h-2 rounded-full transition-all duration-500" style="width: 0%"></div>
                                </div>
                            </div>
                        </div>

                        <div class="mt-4 pt-3 border-t border-slate-200 flex justify-between items-end">
                            <div>
                                <span class="block text-xs text-slate-400 font-semibold uppercase">Xếp loại</span>
                                <span id="detailXL" class="font-bold px-2.5 py-0.5 rounded-full text-xs">Loại</span>
                            </div>
                            <div class="text-right">
                                <span class="block text-xs text-slate-400 font-semibold uppercase">Tổng kết</span>
                                <span id="detailTK" class="text-3xl font-extrabold text-blue-700 leading-none">0.0</span>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- DỰ ĐOÁN ĐIỂM CUỐI KỲ -->
            <section class="bg-white rounded-2xl p-6 border border-slate-200/80 shadow-sm flex flex-col justify-between">
                <div>
                    <h2 class="text-base font-bold text-slate-800 uppercase tracking-wide mb-4 flex items-center gap-2">
                        🎯 3. Dự đoán điểm Cuối kỳ
                    </h2>
                    
                    <div class="space-y-3 bg-slate-50 p-4 rounded-xl border border-slate-200/70">
                        <div>
                            <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Mục tiêu Xếp loại:</label>
                            <select id="calcTarget" class="w-full bg-white border border-slate-300 text-slate-800 text-xs rounded-lg p-2.5 outline-none focus:ring-2 focus:ring-blue-500 font-semibold">
                                <option value="8.5">Loại Giỏi (>= 8.5 điểm)</option>
                                <option value="7.0">Loại Khá (>= 7.0 điểm)</option>
                                <option value="5.0" selected>Đạt Môn (>= 5.0 điểm)</option>
                            </select>
                        </div>
                        <div class="grid grid-cols-2 gap-3">
                            <div>
                                <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Chuyên cần (20%):</label>
                                <input type="number" id="calcCC" min="0" max="10" step="0.5" value="8" class="w-full bg-white border border-slate-300 rounded-lg p-2 text-xs outline-none focus:ring-2 focus:ring-blue-500 font-bold">
                            </div>
                            <div>
                                <label class="block text-xs font-semibold text-slate-600 uppercase mb-1">Giữa kỳ (30%):</label>
                                <input type="number" id="calcGK" min="0" max="10" step="0.5" value="7" class="w-full bg-white border border-slate-300 rounded-lg p-2 text-xs outline-none focus:ring-2 focus:ring-blue-500 font-bold">
                            </div>
                        </div>
                        <button onclick="window.calculateRequiredFinal()" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs py-2.5 rounded-lg shadow-sm transition-all mt-1">
                            🧮 Tính điểm thi cần đạt
                        </button>
                    </div>
                </div>

                <div id="calcResultBox" class="mt-4 p-3.5 bg-blue-50/80 border border-blue-200 rounded-xl flex items-center justify-between">
                    <span class="text-xs text-blue-900 font-medium">Cần thi Cuối kỳ tối thiểu:</span>
                    <span id="calcResultVal" class="text-2xl font-black text-blue-700">4.8 điểm</span>
                </div>
            </section>
        </div>

        <!-- Biểu đồ -->
        <section class="bg-white rounded-2xl p-6 border border-slate-200/80 shadow-sm">
            <h2 class="text-base font-bold text-slate-800 uppercase tracking-wide mb-4 flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> 4. Biểu đồ phân tích tổng quan
            </h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 h-[280px]">
                <div class="md:col-span-2 h-full relative">
                    <canvas id="gradeChart"></canvas>
                </div>
                <div class="md:col-span-1 h-full relative flex items-center justify-center">
                    <canvas id="pieChart"></canvas>
                </div>
            </div>
        </section>

    </div>

    <!-- FOOTER: BẢN QUYỀN -->
    <footer class="mt-8 border-t border-slate-200/80 pt-6 pb-4">
        <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4 text-xs text-slate-500">
            <div class="flex items-center gap-2 text-center md:text-left">
                <span class="font-bold text-slate-700">© 2026 UTH Grade Manager System.</span>
                <span class="hidden sm:inline text-slate-300">•</span>
                <span>Bản quyền thuộc về Nguyễn NGọc Nguyên (UTH).</span>
            </div>
            
            <div class="inline-flex items-center gap-3 bg-white px-4 py-2 rounded-xl border border-slate-200 shadow-sm text-slate-700">
                <span>Tác giả: <b class="text-slate-900 uppercase">Nguyễn Ngọc Nguyên</b></span>
                <span class="text-slate-300">|</span>
                <span>MSSV: <b class="text-slate-900 font-mono">060208009198</b></span>
            </div>

            <div class="text-slate-400 font-medium">
                All Rights Reserved.
            </div>
        </div>
    </footer>

    <script>
        const rawData = [
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

        const students = rawData.map(s => {
            let tongKet = Math.round(((s.cc * 0.2) + (s.gk * 0.3) + (s.ck * 0.5)) * 10) / 10;
            let xepLoai = tongKet >= 8.5 ? 'Giỏi' : tongKet >= 7.0 ? 'Khá' : tongKet >= 5.0 ? 'Trung bình' : 'Yếu';
            let badgeClass = tongKet >= 8.5 ? 'bg-emerald-100 text-emerald-800 border-emerald-200' : 
                             tongKet >= 7.0 ? 'bg-blue-100 text-blue-800 border-blue-200' : 
                             tongKet >= 5.0 ? 'bg-amber-100 text-amber-800 border-amber-200' : 
                             'bg-rose-100 text-rose-800 border-rose-200';
            return { ...s, tongKet, xepLoai, badgeClass };
        });

        const maxScore = Math.max(...students.map(s => s.tongKet));
        let currentFilter = 'All';
        let sortAsc = null;

        // BẢNG ĐIỂM
        window.renderTable = function() {
            try {
                const tableBody = document.getElementById('tableBody');
                const searchVal = (document.getElementById('searchInput')?.value || '').toLowerCase().trim();
                tableBody.innerHTML = '';
                
                let filtered = students.filter(s => {
                    let matchFilter = currentFilter === 'All' || s.xepLoai === currentFilter;
                    let matchSearch = s.name.toLowerCase().includes(searchVal);
                    return matchFilter && matchSearch;
                });

                if (sortAsc !== null) {
                    filtered.sort((a, b) => sortAsc ? a.tongKet - b.tongKet : b.tongKet - a.tongKet);
                }

                if (filtered.length === 0) {
                    tableBody.innerHTML = `<tr><td colspan="7" class="p-6 text-center text-slate-400">Không tìm thấy sinh viên phù hợp</td></tr>`;
                    return;
                }

                filtered.forEach(s => {
                    let isTop = s.tongKet === maxScore;
                    tableBody.innerHTML += `<tr class="hover:bg-slate-50 transition-colors duration-150 animate-fade-in">
                        <td class="p-3.5 text-center text-slate-400 font-medium">${s.id}</td>
                        <td class="p-3.5 font-semibold text-slate-800 flex items-center gap-1.5">
                            ${s.name} ${isTop ? '<span class="text-xs bg-amber-100 text-amber-700 px-1.5 py-0.5 rounded-full font-bold border border-amber-300">⭐ Thủ khoa</span>' : ''}
                        </td>
                        <td class="p-3.5 text-center text-slate-600">${s.cc}</td>
                        <td class="p-3.5 text-center text-slate-600">${s.gk}</td>
                        <td class="p-3.5 text-center text-slate-600">${s.ck}</td>
                        <td class="p-3.5 text-center font-bold text-blue-700 bg-blue-50/40">${s.tongKet}</td>
                        <td class="p-3.5 text-center"><span class="px-2.5 py-1 rounded-full text-xs font-semibold border ${s.badgeClass}">${s.xepLoai}</span></td>
                    </tr>`;
                });
            } catch(e) { console.error("Err renderTable:", e); }
        };

        window.filterTable = function(category) {
            currentFilter = category;
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('bg-white', 'text-blue-700', 'shadow-sm');
                btn.classList.add('text-slate-600');
                if (btn.textContent === (category === 'All' ? 'Tất cả' : category)) {
                    btn.classList.add('bg-white', 'text-blue-700', 'shadow-sm');
                    btn.classList.remove('text-slate-600');
                }
            });
            window.renderTable();
        };

        window.handleSearch = function() { window.renderTable(); };

        window.toggleSort = function() {
            if (sortAsc === null) sortAsc = false;
            else if (sortAsc === false) sortAsc = true;
            else sortAsc = null;
            document.getElementById('sortIcon').textContent = sortAsc === false ? '↓' : sortAsc === true ? '↑' : '⇅';
            window.renderTable();
        };

        // TRA CỨU SINH VIÊN
        window.populateStudentSelect = function() {
            try {
                const select = document.getElementById('studentSelect');
                select.innerHTML = '<option value="" disabled selected>-- Chọn sinh viên để xem --</option>';
                students.forEach(s => {
                    select.innerHTML += `<option value="${s.id}">${s.id}. ${s.name}</option>`;
                });
            } catch(e) { console.error("Err populateSelect:", e); }
        };

        window.handleSelectStudent = function() {
            try {
                const id = document.getElementById('studentSelect').value;
                const s = students.find(x => x.id == id);
                if(s) {
                    document.getElementById('detailAvatar').textContent = s.name.charAt(0);
                    document.getElementById('detailName').textContent = s.name;
                    document.getElementById('detailCC').textContent = s.cc;
                    document.getElementById('detailGK').textContent = s.gk;
                    document.getElementById('detailCK').textContent = s.ck;
                    document.getElementById('detailTK').textContent = s.tongKet;
                    
                    const pct = (s.tongKet / 10) * 100;
                    document.getElementById('progressBar').style.width = pct + '%';
                    document.getElementById('progressText').textContent = pct.toFixed(0) + '%';

                    const xl = document.getElementById('detailXL');
                    xl.textContent = s.xepLoai;
                    xl.className = `font-bold px-2.5 py-0.5 rounded-full text-xs border ${s.badgeClass}`;
                    document.getElementById('studentDetailCard').classList.remove('hidden');
                }
            } catch(e) { console.error("Err handleSelect:", e); }
        };

        // DỰ ĐOÁN ĐIỂM
        window.calculateRequiredFinal = function() {
            try {
                const target = parseFloat(document.getElementById('calcTarget').value);
                const cc = parseFloat(document.getElementById('calcCC').value) || 0;
                const gk = parseFloat(document.getElementById('calcGK').value) || 0;

                let currentPoints = (cc * 0.2) + (gk * 0.3);
                let neededFinal = (target - currentPoints) / 0.5;
                neededFinal = Math.round(neededFinal * 10) / 10;

                const resVal = document.getElementById('calcResultVal');

                if (neededFinal > 10) {
                    resVal.textContent = "Không thể đạt (>10đ)";
                    resVal.className = "text-sm font-bold text-rose-600";
                } else if (neededFinal <= 0) {
                    resVal.textContent = "Đã đủ điểm đạt";
                    resVal.className = "text-sm font-bold text-emerald-600";
                } else {
                    resVal.textContent = `${neededFinal} điểm`;
                    resVal.className = "text-xl font-black text-blue-700";
                }
            } catch(e) { console.error("Err calc:", e); }
        };

        // THỐNG KÊ & CẢNH BÁO
        window.renderStatsAndInsights = function() {
            try {
                const allScores = students.map(s => s.tongKet);
                const avg = (allScores.reduce((a, b) => a + b, 0) / students.length).toFixed(2);
                const minScore = Math.min(...allScores);

                document.getElementById('statsContainer').innerHTML = `
                    <div class="bg-white p-4 rounded-2xl border border-slate-200/80 shadow-sm card-hover">
                        <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Trung bình lớp</p>
                        <p class="text-3xl font-extrabold text-slate-900">${avg}</p>
                    </div>
                    <div class="bg-white p-4 rounded-2xl border border-slate-200/80 shadow-sm card-hover">
                        <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Điểm cao nhất</p>
                        <p class="text-3xl font-extrabold text-emerald-600">${maxScore}</p>
                    </div>
                    <div class="bg-white p-4 rounded-2xl border border-slate-200/80 shadow-sm card-hover">
                        <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Điểm thấp nhất</p>
                        <p class="text-3xl font-extrabold text-rose-600">${minScore}</p>
                    </div>
                    <div class="bg-white p-4 rounded-2xl border border-slate-200/80 shadow-sm card-hover">
                        <p class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1">Số SV đạt (>=5)</p>
                        <p class="text-3xl font-extrabold text-blue-600">${students.filter(s=>s.tongKet>=5).length} <span class="text-sm font-normal text-slate-400">/ 10</span></p>
                    </div>
                `;

                const weakStudents = students.filter(s => s.tongKet < 5.0);
                const textEl = document.getElementById('insightText');
                const badgeEl = document.getElementById('riskStudentsBadge');

                if (weakStudents.length > 0) {
                    textEl.textContent = `Lớp có ${weakStudents.length} sinh viên có nguy cơ không đạt môn (Điểm tổng kết < 5.0). Cần hỗ trợ ôn tập gấp!`;
                    badgeEl.innerHTML = weakStudents.map(s => `<span class="bg-rose-100 text-rose-800 text-xs font-bold px-2 py-0.5 rounded-full border border-rose-300">⚠️ ${s.name} (${s.tongKet}đ)</span>`).join('');
                } else {
                    textEl.textContent = `Tất cả sinh viên trong lớp đều đạt điểm từ 5.0 trở lên. Tiến độ học tập rất tốt!`;
                    badgeEl.innerHTML = `<span class="bg-emerald-100 text-emerald-800 text-xs font-bold px-2 py-0.5 rounded-full border border-emerald-300">🎉 Lớp đạt 100%</span>`;
                }
            } catch(e) { console.error("Err stats:", e); }
        };

        // BIỂU ĐỒ
        window.renderCharts = function() {
            try {
                if (typeof Chart === 'undefined') return;
                const allScores = students.map(s => s.tongKet);

                const ctxBar = document.getElementById('gradeChart')?.getContext('2d');
                if (ctxBar) {
                    const gradBar = ctxBar.createLinearGradient(0, 0, 0, 300);
                    gradBar.addColorStop(0, '#2563eb');
                    gradBar.addColorStop(1, '#0d9488');

                    new Chart(ctxBar, {
                        type: 'bar',
                        data: {
                            labels: students.map(s => s.name),
                            datasets: [{ data: allScores, backgroundColor: gradBar, borderRadius: 6, barPercentage: 0.55 }]
                        },
                        options: {
                            responsive: true, maintainAspectRatio: false,
                            plugins: { legend: { display: false } },
                            scales: { y: { beginAtZero: true, max: 10, grid: { color: '#f1f5f9' } }, x: { grid: { display: false } } }
                        }
                    });
                }

                const ctxPie = document.getElementById('pieChart')?.getContext('2d');
                if (ctxPie) {
                    const countXl = {
                        'Giỏi': students.filter(s => s.xepLoai === 'Giỏi').length,
                        'Khá': students.filter(s => s.xepLoai === 'Khá').length,
                        'Trung bình': students.filter(s => s.xepLoai === 'Trung bình').length,
                        'Yếu': students.filter(s => s.xepLoai === 'Yếu').length,
                    };

                    new Chart(ctxPie, {
                        type: 'doughnut',
                        data: {
                            labels: ['Giỏi', 'Khá', 'Trung bình', 'Yếu'],
                            datasets: [{
                                data: [countXl['Giỏi'], countXl['Khá'], countXl['Trung bình'], countXl['Yếu']],
                                backgroundColor: ['#10b981', '#3b82f6', '#f59e0b', '#f43f5e'],
                                borderWidth: 2, borderColor: '#ffffff'
                            }]
                        },
                        options: {
                            responsive: true, maintainAspectRatio: false,
                            plugins: { legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 10 } } } },
                            cutout: '65%'
                        }
                    });
                }
            } catch(e) { console.error("Err charts:", e); }
        };

        // Khởi tạo
        document.addEventListener('DOMContentLoaded', function() {
            window.renderTable();
            window.renderStatsAndInsights();
            window.populateStudentSelect();
            window.calculateRequiredFinal();
            setTimeout(window.renderCharts, 200);
        });
    </script>
</body>
</html>"""

st.components.v1.html(html_code, height=1350, scrolling=True)
