package uk.co.hackajob.interview.persistence.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import uk.co.hackajob.interview.persistence.Country;

public interface CountryRepository extends JpaRepository<Country, Long> {

}
