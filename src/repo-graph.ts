import * as d3 from 'd3'

type PackageStat = {
    Name: string
    Packages: number
    'Fresh Packages': number
}

const svg = d3.select('svg')
const width = +svg.attr('width') || 800
const height = +svg.attr('height') || 500
const margin = { top: 30, right: 20, bottom: 50, left: 70 }
const innerWidth = width - margin.left - margin.right
const innerHeight = height - margin.top - margin.bottom

const chart = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

// === Load CSV data ===
d3.csv<PackageStat, string>('packages.csv', d3.autoType).then((data) => {
    // Define scales
    const x = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d.Packages)])
        .nice()
        .range([0, innerWidth])

    const y = d3
        .scaleLinear()
        .domain([0, d3.max(data, (d) => d['Fresh Packages'])])
        .nice()
        .range([innerHeight, 0])

    // Add axes
    chart
        .append('g')
        .attr('transform', `translate(0,${innerHeight})`)
        .call(d3.axisBottom(x))
        .append('text')
        .attr('x', innerWidth / 2)
        .attr('y', 40)
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .text('Packages')

    chart
        .append('g')
        .call(d3.axisLeft(y))
        .append('text')
        .attr('x', -innerHeight / 2)
        .attr('y', -50)
        .attr('fill', 'black')
        .attr('text-anchor', 'middle')
        .attr('transform', 'rotate(-90)')
        .text('Fresh Packages')

    // Add points
    chart
        .selectAll('circle')
        .data(data)
        .join('circle')
        .attr('cx', (d) => x(d.Packages))
        .attr('cy', (d) => y(d['Fresh Packages']))
        .attr('r', 5)

    // Add labels
    chart
        .selectAll('text.label')
        .data(data)
        .join('text')
        .attr('class', 'label')
        .attr('x', (d) => x(d.Packages) + 7)
        .attr('y', (d) => y(d['Fresh Packages']))
        .text((d) => d.Name)
})
