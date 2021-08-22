import Tonic from 'https://cdn.skypack.dev/@optoolco/tonic';

class LeadDemo extends Tonic {
    stylesheet() {
        if (this.props.loadedALGX) {
            return `
                .example-viz {
                    display: grid;
                    grid-template-rows: auto 1fr;
                    height: 100%;
                    width: 100%;
                    grid-template-columns: 1fr
                }
                .example-viz > .algx {
                    width: 100%;
                    height: calc(100% - var(--mu))
                }
                .example-viz > .button-container {
                    padding: var(--mu);
                    width: 100%
                }
                .example-viz > .button-container > button {
                    width: 100%
                }
            `
        }
        return `
            .example-viz {
                display: grid;
                align-items: center;
                justify-content: center;
                align-self: center;
            }
        `
    }
    constructor () {
        super()
    }
    async connected () {
        this.props.loadedALGX = false
        const { createCanvas } = await import('https://cdn.skypack.dev/pin/algorithmx@v2.0.2-XNeB0GMuUYszkBPez6Pc/mode=imports,min/optimized/algorithmx.js');
        this.props.loadedALGX = true
        await this.reRender()
        const el = document.querySelector(`#demoPyNode`)
        console.log(el)
		const g = createCanvas(el);
        this.props.g = g
        this.props.el = el
        this.resetGraph()
    }

    resetGraph () {
		const g = this.props.g;
		g.duration(0).withQ(null).remove();
    g.queues().clear().start();
		try {
			g.duration(0).attrs({
				svgattrs: { width: '100%' },
				size: [this.props.el.getBoundingClientRect().width, this.props.el.getBoundingClientRect().height],
				zoomtoggle: true,
			})
		} catch {}
        //this.reRender()
	}

    click (e) {
		if (!e.target.matches('#play')) return
        const g = this.props.g
		this.resetGraph()
        console.log(g)
        'abc'.split('').forEach(i => {
            g.node(i).add();
            g.pause(0.1)
        });
        g.pause(0.5)
        g.edge('ab').add()
        g.edge('bc').add()
	}

    render () {
        if (this.props.loadedALGX) {
            return this.html`
                <div class="button-container">
                    <button id="play">RUN</button>
                </div>
                <div class="algx" id="demoPyNode"></div>
              
            `
        }
        return this.html`
            <div class="loading-spinner"></div>
        `
    }
}

Tonic.add(LeadDemo)