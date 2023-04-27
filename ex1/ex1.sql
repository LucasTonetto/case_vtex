-- Query realizada no BigQuery
SELECT 
  Cliente,
  DATE_DIFF(CURRENT_DATE(), MAX(Data), DAY) AS recencia,
  COUNT(*) AS frequencia,
  SUM(valor) AS valor_total
FROM `projeot.dataset.tabela`
GROUP BY Cliente