/**
 * ContentFlow — Lightweight Canvas Charting
 * LineChart, BarChart, CircularProgress, renderSparkline
 */

const COLORS = {
  primary: '#7c3aed',
  primaryLight: '#a78bfa',
  accent: '#06b6d4',
  accentLight: '#67e8f9',
  success: '#22c55e',
  warning: '#eab308',
  danger: '#ef4444',
  text: '#f1f0ff',
  textMuted: '#6b6890',
  surface: '#1a1a2e',
  grid: 'rgba(124, 58, 237, 0.08)',
  linkedin: '#0077B5',
  instagram: '#e6683c',
  youtube: '#FF0000',
};

/**
 * LineChart — draws animated line chart on a canvas.
 */
export class LineChart {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = {
      padding: { top: 30, right: 20, bottom: 40, left: 50 },
      lineWidth: 2.5,
      dotRadius: 4,
      gridLines: 5,
      showDots: true,
      showArea: true,
      animate: true,
      colors: [COLORS.primary, COLORS.accent, COLORS.success],
      ...options,
    };
    this.datasets = [];
    this.labels = [];
    this.animProgress = 0;
    this._resize();
    window.addEventListener('resize', () => this._resize());
  }

  _resize() {
    const parent = this.canvas.parentElement;
    if (!parent) return;
    const dpr = window.devicePixelRatio || 1;
    const w = parent.clientWidth;
    const h = this.options.height || 220;
    this.canvas.width = w * dpr;
    this.canvas.height = h * dpr;
    this.canvas.style.width = w + 'px';
    this.canvas.style.height = h + 'px';
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.w = w;
    this.h = h;
    if (this.datasets.length) this._draw(1);
  }

  setData(labels, datasets) {
    this.labels = labels;
    this.datasets = datasets; // [{label, data, color?}]
    if (this.options.animate) {
      this._animate();
    } else {
      this._draw(1);
    }
  }

  _animate() {
    this.animProgress = 0;
    const start = performance.now();
    const duration = 800;
    const step = (now) => {
      this.animProgress = Math.min((now - start) / duration, 1);
      this._draw(this.animProgress);
      if (this.animProgress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  _draw(progress) {
    const { ctx, w, h, options: o, labels, datasets } = this;
    const { top, right, bottom, left } = o.padding;
    const chartW = w - left - right;
    const chartH = h - top - bottom;

    ctx.clearRect(0, 0, w, h);

    // Compute y range
    let allValues = datasets.flatMap(d => d.data);
    let yMin = Math.min(0, ...allValues);
    let yMax = Math.max(...allValues) * 1.1 || 100;

    // Grid
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    for (let i = 0; i <= o.gridLines; i++) {
      const y = top + (i / o.gridLines) * chartH;
      ctx.beginPath();
      ctx.moveTo(left, y);
      ctx.lineTo(left + chartW, y);
      ctx.stroke();

      // Labels
      const val = yMax - (i / o.gridLines) * (yMax - yMin);
      ctx.fillStyle = COLORS.textMuted;
      ctx.font = '11px Inter';
      ctx.textAlign = 'right';
      ctx.fillText(Math.round(val), left - 8, y + 4);
    }
    ctx.setLineDash([]);

    // X labels
    const step = labels.length > 1 ? chartW / (labels.length - 1) : chartW;
    ctx.fillStyle = COLORS.textMuted;
    ctx.font = '11px Inter';
    ctx.textAlign = 'center';
    labels.forEach((label, i) => {
      ctx.fillText(label, left + i * step, h - 8);
    });

    // Draw datasets
    datasets.forEach((dataset, di) => {
      const color = dataset.color || o.colors[di % o.colors.length];
      const data = dataset.data;
      const len = Math.ceil(data.length * progress);

      ctx.strokeStyle = color;
      ctx.lineWidth = o.lineWidth;
      ctx.lineJoin = 'round';
      ctx.lineCap = 'round';
      ctx.beginPath();

      const points = [];
      for (let i = 0; i < len; i++) {
        const x = left + i * step;
        const y = top + chartH - ((data[i] - yMin) / (yMax - yMin)) * chartH;
        points.push({ x, y });
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Area
      if (o.showArea && points.length > 1) {
        const gradient = ctx.createLinearGradient(0, top, 0, top + chartH);
        gradient.addColorStop(0, color + '30');
        gradient.addColorStop(1, color + '00');
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.moveTo(points[0].x, points[0].y);
        points.forEach(p => ctx.lineTo(p.x, p.y));
        ctx.lineTo(points[points.length - 1].x, top + chartH);
        ctx.lineTo(points[0].x, top + chartH);
        ctx.closePath();
        ctx.fill();
      }

      // Dots
      if (o.showDots) {
        points.forEach(p => {
          ctx.fillStyle = '#0a0a12';
          ctx.beginPath();
          ctx.arc(p.x, p.y, o.dotRadius + 1, 0, Math.PI * 2);
          ctx.fill();

          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.arc(p.x, p.y, o.dotRadius, 0, Math.PI * 2);
          ctx.fill();
        });
      }
    });
  }
}

/**
 * BarChart — draws animated bar chart.
 */
export class BarChart {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = {
      padding: { top: 30, right: 20, bottom: 40, left: 50 },
      barWidth: 0.6,
      animate: true,
      colors: [COLORS.linkedin, COLORS.instagram, COLORS.youtube, COLORS.primary],
      borderRadius: 6,
      ...options,
    };
    this.data = [];
    this.labels = [];
    this._resize();
    window.addEventListener('resize', () => this._resize());
  }

  _resize() {
    const parent = this.canvas.parentElement;
    if (!parent) return;
    const dpr = window.devicePixelRatio || 1;
    const w = parent.clientWidth;
    const h = this.options.height || 220;
    this.canvas.width = w * dpr;
    this.canvas.height = h * dpr;
    this.canvas.style.width = w + 'px';
    this.canvas.style.height = h + 'px';
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    this.w = w;
    this.h = h;
    if (this.data.length) this._draw(1);
  }

  setData(labels, data, colors) {
    this.labels = labels;
    this.data = data;
    this.barColors = colors || this.options.colors;
    if (this.options.animate) {
      this._animate();
    } else {
      this._draw(1);
    }
  }

  _animate() {
    const start = performance.now();
    const duration = 600;
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      this._draw(eased);
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }

  _draw(progress) {
    const { ctx, w, h, options: o, labels, data, barColors } = this;
    const { top, right, bottom, left } = o.padding;
    const chartW = w - left - right;
    const chartH = h - top - bottom;

    ctx.clearRect(0, 0, w, h);

    const yMax = Math.max(...data) * 1.15 || 100;

    // Grid
    ctx.strokeStyle = COLORS.grid;
    ctx.lineWidth = 1;
    ctx.setLineDash([4, 4]);
    for (let i = 0; i <= 4; i++) {
      const y = top + (i / 4) * chartH;
      ctx.beginPath();
      ctx.moveTo(left, y);
      ctx.lineTo(left + chartW, y);
      ctx.stroke();
      ctx.fillStyle = COLORS.textMuted;
      ctx.font = '11px Inter';
      ctx.textAlign = 'right';
      ctx.fillText(Math.round(yMax - (i / 4) * yMax), left - 8, y + 4);
    }
    ctx.setLineDash([]);

    // Bars
    const groupW = chartW / data.length;
    const barW = groupW * o.barWidth;

    data.forEach((val, i) => {
      const x = left + i * groupW + (groupW - barW) / 2;
      const barH = (val / yMax) * chartH * progress;
      const y = top + chartH - barH;
      const color = barColors[i % barColors.length];

      // Shadow
      ctx.fillStyle = color + '25';
      ctx.fillRect(x - 2, y + 4, barW + 4, barH);

      // Bar with rounded top
      const r = Math.min(o.borderRadius, barW / 2, barH);
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.moveTo(x, y + r);
      ctx.arcTo(x, y, x + r, y, r);
      ctx.arcTo(x + barW, y, x + barW, y + r, r);
      ctx.lineTo(x + barW, top + chartH);
      ctx.lineTo(x, top + chartH);
      ctx.closePath();
      ctx.fill();

      // Label
      ctx.fillStyle = COLORS.textMuted;
      ctx.font = '11px Inter';
      ctx.textAlign = 'center';
      ctx.fillText(labels[i] || '', x + barW / 2, h - 8);

      // Value on top
      if (progress > 0.9) {
        ctx.fillStyle = COLORS.text;
        ctx.font = 'bold 12px Inter';
        ctx.fillText(Math.round(val), x + barW / 2, y - 8);
      }
    });
  }
}

/**
 * CircularProgress — animated circular meter.
 */
export class CircularProgress {
  constructor(canvas, options = {}) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.options = {
      size: 120,
      lineWidth: 10,
      bgColor: 'rgba(124, 58, 237, 0.1)',
      animate: true,
      ...options,
    };
    this.value = 0;
    this._setup();
  }

  _setup() {
    const dpr = window.devicePixelRatio || 1;
    const s = this.options.size;
    this.canvas.width = s * dpr;
    this.canvas.height = s * dpr;
    this.canvas.style.width = s + 'px';
    this.canvas.style.height = s + 'px';
    this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  getColor(val) {
    if (val < 40) return COLORS.danger;
    if (val < 70) return COLORS.warning;
    return COLORS.success;
  }

  setValue(value, color) {
    const target = Math.min(Math.max(value, 0), 100);
    const c = color || this.getColor(target);
    if (this.options.animate) {
      this._animate(this.value, target, c);
    } else {
      this.value = target;
      this._draw(target, c);
    }
  }

  _animate(from, to, color) {
    const start = performance.now();
    const duration = 1000;
    const step = (now) => {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      const current = from + (to - from) * eased;
      this._draw(current, color);
      if (p < 1) requestAnimationFrame(step);
      else this.value = to;
    };
    requestAnimationFrame(step);
  }

  _draw(val, color) {
    const { ctx, options: o } = this;
    const s = o.size;
    const cx = s / 2;
    const cy = s / 2;
    const r = (s - o.lineWidth) / 2;

    ctx.clearRect(0, 0, s, s);

    // Background arc
    ctx.strokeStyle = o.bgColor;
    ctx.lineWidth = o.lineWidth;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.stroke();

    // Value arc
    const startAngle = -Math.PI / 2;
    const endAngle = startAngle + (val / 100) * Math.PI * 2;

    const gradient = ctx.createLinearGradient(0, 0, s, s);
    gradient.addColorStop(0, color);
    gradient.addColorStop(1, color + 'aa');

    ctx.strokeStyle = gradient;
    ctx.lineWidth = o.lineWidth;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.arc(cx, cy, r, startAngle, endAngle);
    ctx.stroke();

    // Glow
    ctx.shadowColor = color;
    ctx.shadowBlur = 12;
    ctx.strokeStyle = color + '60';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(cx, cy, r, startAngle, endAngle);
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Center value
    ctx.fillStyle = COLORS.text;
    ctx.font = `bold ${s * 0.22}px Outfit`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(Math.round(val), cx, cy);
  }
}

/**
 * Render a tiny sparkline into a canvas.
 */
export function renderSparkline(canvas, data, color = COLORS.primary) {
  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const w = canvas.parentElement?.clientWidth || 100;
  const h = 32;
  canvas.width = w * dpr;
  canvas.height = h * dpr;
  canvas.style.width = w + 'px';
  canvas.style.height = h + 'px';
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

  if (!data.length) return;

  const min = Math.min(...data);
  const max = Math.max(...data) || 1;
  const range = max - min || 1;
  const step = w / (data.length - 1 || 1);
  const pad = 4;

  ctx.strokeStyle = color;
  ctx.lineWidth = 1.5;
  ctx.lineJoin = 'round';
  ctx.beginPath();

  data.forEach((val, i) => {
    const x = i * step;
    const y = pad + ((max - val) / range) * (h - pad * 2);
    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Gradient fill
  const gradient = ctx.createLinearGradient(0, 0, 0, h);
  gradient.addColorStop(0, color + '30');
  gradient.addColorStop(1, color + '00');
  ctx.lineTo(w, h);
  ctx.lineTo(0, h);
  ctx.closePath();
  ctx.fillStyle = gradient;
  ctx.fill();
}
