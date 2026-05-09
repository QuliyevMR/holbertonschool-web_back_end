export default function createIteratorObject(report) {
  const allEmployees = [];

  // Bütün departamentlərdəki işçiləri tək bir massivə yığırıq
  for (const department of Object.values(report.allEmployees)) {
    allEmployees.push(...department);
  }

  // Massivin öz iteratorunu qaytarırıq
  return allEmployees[Symbol.iterator]();
}
