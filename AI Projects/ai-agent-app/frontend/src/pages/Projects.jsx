import portfolio from '../../../portfolio.json';

export default function Projects() {
  return <main><h1 className="text-3xl font-bold mb-4">Projects</h1>
    <p className="mb-6">Explore the problem, source, evaluation and limits directly. No chat account or API key is needed.</p>
    <div className="grid gap-6 md:grid-cols-3">{portfolio.projects.map(project => <article key={project.id} className="bg-white rounded-lg p-6 shadow-md">
      <h2 className="text-xl font-semibold mb-3">{project.name}</h2><p>{project.description}</p>
      <p className="my-3">{project.stack.join(' · ')}</p>
      <a className="text-blue-700 underline" href={project.url}>Read source and evidence</a>
    </article>)}</div>
  </main>;
}
