# Researchplan

> **Status 2026-09-02:** Researchpass v1 genomfört. Resultat finns i `docs/researchresultat-v1.md`; källor i `docs/kallregister.md`. Planen behålls som styrning för just-in-time-komplettering under manusarbetet.

## Syfte

Researchpasset ska ge en robust faktabas och pröva bokens pedagogiska mognadsmodell. Målet är inte att hitta citat som bekräftar modellen, utan att aktivt söka efter data som kan nyansera eller motsäga den.

## Forskningsfrågor

### 1. Förändras AI-användningen med erfarenhet?

Undersök:

- om användare breddar antalet uppgiftstyper över tid,
- om användningen går från informationssökning mot produktion och handling,
- om längre erfarenhet leder till mer kontext, iteration eller delegering,
- om det finns alternativa mognadsmodeller som bör påverka bokens sju faser.

### 2. Hur används AI i systemutvecklingsprocessen?

Undersök separat:

- krav och analys,
- design och arkitektur,
- implementation,
- test och kvalitet,
- DevOps/CI/CD och drift,
- dokumentation och kunskapsarbete.

Identifiera både vanlig användning och aktiviteter där användare är mer tveksamma.

### 3. När ger AI produktivitetsvinster?

Jämför:

- självrapporterad produktivitet,
- experimentellt uppmätt produktivitet,
- kvalitet och omarbete,
- nybörjare kontra erfarna personer,
- greenfield kontra befintliga komplexa system,
- lokal aktivitetshastighet kontra total genomloppstid.

### 4. Hur förändras människans roll?

Undersök forskning om:

- problemformulering,
- verifiering,
- cognitive offloading,
- automation bias,
- kompetensutveckling och eventuell deskilling,
- förskjutning mellan yrkesroller och arbetsuppgifter.

### 5. Vad vet vi om agentiska och delegerade arbetsflöden?

Undersök:

- coding agents och andra verktygsanvändande agenter,
- hur autonomi påverkar kvalitet och risk,
- vilka kontrollpunkter som rekommenderas,
- skillnaden mellan demos/benchmarks och verkligt arbete.

### 6. Hur bör icke-publikt material hanteras?

Jämför aktuella villkor och tekniska skydd för relevanta tjänstekategorier:

- konsumenttjänster,
- business/enterprise-tjänster,
- API-tjänster,
- molnplattformars managed AI-tjänster,
- kodassistenter och IDE-integrationer,
- connectors och externa verktyg.

Separera uttryckligen:

- modellträning,
- lagring/retention,
- loggning,
- support-/administratörsåtkomst,
- data residency,
- underleverantörer,
- behörighet,
- webbsökning/verktygsanrop,
- organisatorisk informationsklassning.

## Källstrategi

Prioritera i denna ordning:

1. peer-reviewad forskning och tydligt dokumenterade experiment,
2. oberoende forskningsorganisationer,
3. stora återkommande utvecklarundersökningar,
4. officiell produkt- och säkerhetsdokumentation för konkreta tjänsteegenskaper,
5. leverantörsstudier som kompletterande data, tydligt märkta med avsändare,
6. välgrundade praktikerfarenheter för exempel, inte som ensam grund för generella påståenden.

## Leverantörer och ekosystem som bör täckas

Minst:

- OpenAI / ChatGPT,
- Anthropic / Claude,
- Google / Gemini,
- GitHub Copilot,
- Microsoft Copilot och relevanta Azure-erbjudanden.

Komplettera vid behov med andra verktyg om de representerar ett särskilt arbetssätt snarare än bara ytterligare en produkt.

## Oberoende källspår

Sök särskilt efter:

- Stack Overflow Developer Survey,
- DORA,
- METR,
- akademiska studier om AI-assisterad programmering,
- studier av människa–AI-samarbete och automation bias,
- empiriska studier av coding agents och längre arbetsuppgifter.

## Källhantering i manus

Varje centralt sakpåstående ska klassificeras som något av:

- **Empiriskt belagt:** stöds av studie/data.
- **Leverantörsspecifikt:** gäller en viss tjänst eller avtalsmodell.
- **Observerat användningsmönster:** stöds av flera erfarenhetskällor men inte nödvändigtvis kausalt belagt.
- **Bokens syntes:** vår pedagogiska modell eller slutsats.

Boken ska vara tydlig med dessa skillnader.
