import portfolio from '../../../portfolio.json';

export default function Career() {
  return <main className="max-w-3xl"><h1 className="text-3xl font-bold mb-4">{portfolio.name}</h1>
    <p className="text-lg mb-4">{portfolio.focus}</p><p className="mb-4">{portfolio.experience_summary}</p>
    <p className="mb-6">{portfolio.study}</p>
    <p>See the Projects page for concrete lab evidence. No employment history, certifications or expert ratings are inferred from a template.</p>
  </main>;
}
