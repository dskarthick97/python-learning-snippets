CREATE TABLE IF NOT EXISTS `scheduler` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `job_name` VARCHAR(255) NOT NULL,
  `trigger_type` ENUM('date', 'interval', 'cron') NOT NULL,
  `trigger_args` JSON,
  `create_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `tracker` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `scheduler_id` INTEGER NOT NULL,
  `create_ts` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- delete range of records
DELETE FROM
  `scheduler`
WHERE
  `id` BETWEEN 6
  AND 15;

-- select records beginning from specific id
SELECT
  *
FROM
  `tracker`
WHERE
  id > 6;

-- select last row in a table
SELECT
  *
FROM
  `tracker`
ORDER BY
  `id` DESC
LIMIT
  1;

SELECT
  *
FROM
  `tracker`
WHERE
  `id` = (
    SELECT
      max(`id`)
    FROM
      `tracker
  );

-- checking whether a row exists in a table
SELECT EXISTS (SELECT 1 FROM `scheduler` WHERE `id` = '37' LIMIT 1);
