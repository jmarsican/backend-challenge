package uk.co.hackajob.interview.persistence.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import uk.co.hackajob.interview.persistence.Currency;

import java.util.Optional;

public interface CurrencyRepository extends JpaRepository<Currency, Long> {

    Optional<Currency> findCurrencyByCode(String currencyCode);
    
}
